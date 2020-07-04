import React from "react";

import moment from "moment-timezone";
import { TableDragSelect } from "./TableDragSelect";

const { Login, Timerange, Timeranges } = require("../../proto/hermes_pb.js");
const { GatewayPromiseClient } = require("../../proto/hermes_grpc_web_pb.js");

export default class Calendar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      gateway: new GatewayPromiseClient(process.env.REACT_APP_BACKEND),
    };
    // moment.tz.setDefault("America/New_York");
  }

  static getDerivedStateFromProps(props, state) {
    if (props.hours !== state.hours || props.days !== state.days) {
      console.log("getDerivedStateFromProps");

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

  // todo this should be static
  createTable = () => {
    let parent = [];

    // moment.tz.setDefault("America/New_York");
    moment.tz.setDefault("");

    for (let i = 0; i < this.props.hours; i++) {
      let children = [];
      for (let j = 0; j < this.props.days; j++) {
        const timestamp = this.state.timestamps[i][j];
        const key = { i: i, j: j };

        if (i === 0 && j === 0) {
          children.push(<td key={key} disabled></td>);
        } else if (j === 0) {
          children.push(
            <td key={key} disabled>
              <pre>{timestamp.format("HHmm")}</pre>
            </td>
          );
        } else if (i === 0) {
          children.push(
            <td key={key} disabled>
              <pre>{timestamp.format("ddd Do")}</pre>
            </td>
          );
        } else {
          children.push(
            <td
              key={key}
              disabled={
                moment().subtract(1799, "seconds") > timestamp ? true : false
              }
            >
              {/* {timestamp.format("")} */}
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
    for (let i = 0; i < hours; i++) {
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

    // moment.tz.setDefault("America/New_York");
    moment.tz.setDefault("");

    for (let i = 0; i < hours; i++) {
      let children = [];
      for (let j = 0; j < days; j++) {
        children.push(
          moment()
            .startOf("day")
            .add(j - 1, "days")
            .add(Math.max(0, i - 1) * 30, "minutes")
        );
      }
      parent.push(children);
    }
    return parent;
  };

  static processTimeranges = (timestamps, timeranges, days, hours) => {
    console.log("processTimeranges", timestamps, timeranges, days, hours);
    let cells = Calendar.createCells(days, hours);
    if (timeranges) {
      for (let i = 0; i < hours; i++) {
        for (let j = 0; j < days; j++) {
          const check = timeranges.some((timerange) => {
            return timestamps[i][j].isSame(timerange);
          });
          if (check) {
            console.log("ok");
            cells[i][j] = true;
          }
        }
      }
    }
    return { timeranges: timeranges, cells: cells };
  };

  update = (cells) => {
    let timestamps = [];

    for (let i = 1; i < this.props.hours; i++) {
      for (let j = 1; j < this.props.days; j++) {
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
      <TableDragSelect
        value={this.state.cells}
        onChange={(cells) => this.update(cells)}
      >
        {this.createTable()}
      </TableDragSelect>
    );
  };
}
