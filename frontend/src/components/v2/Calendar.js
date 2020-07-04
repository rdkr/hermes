import React from "react";

import moment from "moment-timezone";
import { TableDragSelect } from "./TableDragSelect";

const { Login, Timerange, Timeranges } = require("../../proto/hermes_pb.js");
const { GatewayPromiseClient } = require("../../proto/hermes_grpc_web_pb.js");

export default class Calendar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      days: 9,
      hours: 49
    }
    this.state = {
      days: 9,
      hours: 49,
      cells: this.createCells(),
      timestamps: this.createTimestamps(),
      gateway: new GatewayPromiseClient(process.env.REACT_APP_BACKEND),
    };
    // moment.tz.setDefault("America/New_York");
  }

  async componentDidMount() {
    this.reloadCalendar();
  }

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

  createCells = () => {
    let parent = [];
    for (let i = 0; i < this.props.hours; i++) {
      let children = [];
      for (let j = 0; j < this.props.days; j++) {
        children.push(false);
      }
      parent.push(children);
    }
    return parent;
  };

  createTimestamps = () => {
    let parent = [];

    // moment.tz.setDefault("America/New_York");
    moment.tz.setDefault("");

    for (let i = 0; i < this.props.hours; i++) {
      let children = [];
      for (let j = 0; j < this.props.days; j++) {
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

  update = (cells) => {
    let timestamps = [];

    for (let i = 1; i < this.props.hours; i++) {
      for (let j = 1; j < this.props.days; j++) {
        if (cells[i][j] === true) {
          timestamps.push(this.state.timestamps[i][j]);
        }
      }
    }

    // console.log("A:", timestamps)
    let timeranges = timestamps.map((timestamp) => {
      let timerange = new Timerange();
      timerange.setStart(moment(timestamp).unix());
      timerange.setEnd(moment(timestamp).add(30, "minutes").unix());
      return timerange;
    });
    // console.log("B:", timeranges)

    const timerangesPb = new Timeranges();
    timerangesPb.setToken(localStorage.getItem("token"));
    timerangesPb.setEvent("radhakr/dnd");
    timerangesPb.setTimerangesList(timeranges);

    this.state.gateway
      .putTimeranges(timerangesPb, {})
      .then((response) => {
        const timeranges = response.getTimerangesList().map((timerange) => {
          return moment.unix(timerange.getStart());
        });

        let cells = this.createCells();
        for (let i = 0; i < this.props.hours; i++) {
          for (let j = 0; j < this.props.days; j++) {
            const check = timeranges.some((timerange) => {
              return this.state.timestamps[i][j].isSame(timerange);
            });
            if (check) {
              cells[i][j] = true;
            }
          }
        }
        this.setState({ cells });
      })
      .catch((err) => {
        console.error(`error: ${err.code}, "${err.message}"`);
      });
  };

  reloadCalendar = () => {
    var login = new Login();
    login.setToken(localStorage.getItem("token"));
    login.setEvent("radhakr/dnd");

    this.state.gateway
      .getTimeranges(login, {})
      .then((response) => {
        const intervals = response
          .getTimerangesList()
          .filter((timerange) => {
            return moment.unix(timerange.getEnd()) > moment.now();
          })
          .map((timerange) => {
            const start = moment.unix(timerange.getStart());
            const end = moment.unix(timerange.getEnd());

            let cells = [];
            for (let i = 0; i < this.props.hours; i++) {
              let children = [];
              for (let j = 0; j < this.props.days; j++) {
                if (
                  this.state.cells[i][j] === true ||
                  this.state.timestamps[i][j].isBetween(
                    start,
                    end,
                    undefined,
                    "[)"
                  )
                ) {
                  children.push(true);
                } else {
                  children.push(false);
                }
              }
              cells.push(children);
            }

            this.setState({ cells });
          });
      })
      .catch((err) => {
        console.error(`hermes error: ${err.code}, "${err.message}"`);
      });
  };

  render = () => (
    <TableDragSelect
      value={this.state.cells}
      onChange={(cells) => this.update(cells)}
    >
      {this.createTable()}
    </TableDragSelect>
  );
}
