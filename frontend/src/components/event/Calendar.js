import React from "react";

import moment from "moment-timezone";
import TableDragSelect from "./TableDragSelect";
import LinearProgress from "@material-ui/core/LinearProgress";

const { Login, Timerange, Timeranges } = require("../../proto/hermes_pb.js");
const { GatewayPromiseClient } = require("../../proto/hermes_grpc_web_pb.js");

export default class Calendar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      gateway: new GatewayPromiseClient(process.env.REACT_APP_BACKEND),
    };
    // moment.tz.setDefault("America/New_York");
    moment.tz.setDefault("");
  }

  static getDerivedStateFromProps(props, state) {
    if (props.hours !== state.hours || props.days !== state.days) {
      const timestamps = Calendar.createTimestamps(props.days, props.hours);
      const processed = Calendar.processTimeranges(
        timestamps,
        state.timeranges,
        props.days,
        props.hours
      );
      return {
        days: props.days,
        hours: props.hours,
        timestamps: timestamps,
        cells: processed.cells,
        timeranges: processed.timeranges,
      };
    }
    return {};
  }

  async componentDidMount() {
    this.reloadCalendar();
  }

  static createTable = (timestamps, disableEntry) => {
    let parent = [];

    for (let i = 0; i < timestamps.length; i++) {
      let children = [];
      for (let j = 0; j < timestamps[i].length; j++) {
        const timestamp = timestamps[i][j];
        const key = timestamp.unix();

        if (i === 0 && j === 0) {
          children.push(
            <td key={key} className={"never-enabled"} disabled></td>
          );
        } else if (j === 0) {
          children.push(
            <td key={key} className={"never-enabled"} disabled>
              <pre>{timestamp.format("HHmm")}</pre>
            </td>
          );
        } else if (i === 0) {
          children.push(
            <td key={key} className={"never-enabled"} disabled>
              <pre>{timestamp.format("ddd Do")}</pre>
            </td>
          );
        } else {
          const timePassed =
            moment().subtract(1799, "seconds") > timestamp ? true : false;
          children.push(
            <td
              key={key}
              className={timePassed ? " never-enabled" : ""}
              disabled={disableEntry || timePassed ? true : false}
            >
              <pre>{timestamp.format("HHmm")}</pre>
            </td>
          );
        }
      }
      parent.push(<tr key={{ row: i }}>{children}</tr>);
    }

    return parent;
  };

  static createCells = (days, hours) => {
    let parent = [];
    for (let i = 0; i < hours[1] - hours[0]; i++) {
      let children = [];
      for (let j = 0; j < days; j++) {
        children.push(false);
      }
      parent.push(children);
    }
    return parent;
  };

  static createTimestamps = (days, hours) => {
    let parent = [];
    for (let i = 0; i < hours[1] - hours[0]; i++) {
      let children = [];
      for (let j = 0; j < days; j++) {
        const t = moment()
          .startOf("day")
          .add(j - 1, "days")
          .add(Math.max(0, i + hours[0] - 1) * 30, "minutes");
        children.push(t);
      }
      parent.push(children);
    }
    return parent;
  };

  static processTimeranges = (timestamps, timeranges, days, hours) => {
    let cells = Calendar.createCells(days, hours);
    if (timeranges) {
      for (let i = 0; i < cells.length; i++) {
        for (let j = 0; j < cells[i].length; j++) {
          const check = timeranges.some((timerange) => {
            return timestamps[i][j].isSame(timerange);
          });
          if (check) {
            cells[i][j] = true;
          }
        }
      }
    }
    return { timeranges: timeranges, cells: cells };
  };

  update = (cells) => {
    this.setState({ disableEntry: true });
    let timestamps = [];

    for (let i = 1; i < cells.length; i++) {
      for (let j = 1; j < cells[i].length; j++) {
        if (cells[i][j] === true) {
          timestamps.push(this.state.timestamps[i][j]);
        }
      }
    }

    let timeranges = timestamps.map((timestamp) => {
      let timerange = new Timerange();
      timerange.setStart(moment(timestamp).unix());
      timerange.setEnd(moment(timestamp).add(30, "minutes").unix());
      return timerange;
    });

    const timerangesPb = new Timeranges();
    timerangesPb.setToken(localStorage.getItem("token"));
    timerangesPb.setEvent(this.props.event);
    timerangesPb.setTimerangesList(timeranges);

    this.state.gateway
      .putTimeranges(timerangesPb, {})
      .then((response) => {
        const timeranges = response.getTimerangesList().map((timerange) => {
          return moment.unix(timerange.getStart());
        });
        this.setState(
          Calendar.processTimeranges(
            this.state.timestamps,
            timeranges,
            this.state.days,
            this.state.hours
          )
        );
      })
      .catch((err) => {
        console.error(`error: ${err.code}, "${err.message}"`);
      })
      .then(() => {
        this.setState({ disableEntry: false });
      });
  };

  reloadCalendar = () => {
    var login = new Login();
    login.setToken(localStorage.getItem("token"));
    login.setEvent(this.props.event);

    this.state.gateway
      .getTimeranges(login, {})
      .then((response) => {
        const timeranges = response.getTimerangesList().map((timerange) => {
          return moment.unix(timerange.getStart());
        });
        this.setState(
          Calendar.processTimeranges(
            this.state.timestamps,
            timeranges,
            this.state.days,
            this.state.hours
          )
        );
      })
      .catch((err) => {
        console.error(`hermes error: ${err.code}, "${err.message}"`);
      });
  };

  render = () => {
    return (
        <div>
        {this.state.disableEntry ? <LinearProgress /> : null}

      <div className={this.state.disableEntry ? "blur" : null}>
        <TableDragSelect
          value={this.state.cells}
          onChange={(cells) => this.update(cells)}
          key={this.state.disableEntry}
        >
          {Calendar.createTable(this.state.timestamps, this.state.disableEntry)}
        </TableDragSelect>
      </div></div>
    );
  };
}
