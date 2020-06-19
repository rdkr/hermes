import React from "react";
import moment from "moment-timezone";
import WeekCalendar from "react-week-calendar";

const { Login, Timerange, Timeranges } = require("./proto/hermes_pb.js");
const { GatewayPromiseClient } = require("./proto/hermes_grpc_web_pb.js");

export default class StandardCalendar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedIntervals: [],
    };
  }

  async componentDidMount() {
    let search = window.location.search;
    let params = new URLSearchParams(search);

    await this.setState({
      gateway: new GatewayPromiseClient(process.env.REACT_APP_BACKEND),
      token: params.get("token"),
      event: params.get("event")
    });

    this.reloadCalendar();
  }

  handleEventRemove = (event) => {
    let timerange = new Timerange();

    const { selectedIntervals } = this.state;
    const index = selectedIntervals.findIndex(
      (interval) => interval.uid === event.uid
    );
    timerange.setId(selectedIntervals[index].uid);

    const timeranges = new Timeranges();
    timeranges.setToken(this.state.token);
    timeranges.setTimerangesList([timerange])

    this.state.gateway
      .deleteTimeranges(timeranges, {})
      .then((response) => {
        this.reloadCalendar();
      })
      .catch((err) => {
        console.error(`error: ${err.code}, "${err.message}"`);
      });
  };

  handleSelect = (newIntervals) => {
    const timeranges = new Timeranges();
    timeranges.setToken(this.state.token);
    timeranges.setEvent(this.state.event);
    timeranges.setTimerangesList(
      newIntervals.map((interval) => {
        let timerange = new Timerange();
        timerange.setStart(interval.start.unix());
        timerange.setEnd(interval.end.unix());
        return timerange;
      })
    );

    this.state.gateway
      .setTimeranges(timeranges, {})
      .then((response) => {
        this.reloadCalendar();
      })
      .catch((err) => {
        console.error(`error: ${err.code}, "${err.message}"`);
      });
  };

  reloadCalendar = () => {

    var login = new Login();
    login.setToken(this.state.token);
    login.setEvent(this.state.event);

    this.state.gateway
      .getTimeranges(login, {})
      .then((response) => {
        const intervals = response.getTimerangesList().map((timerange) => {
          const startDatetime = moment.tz(
            moment.unix(timerange.getStart()).utc(),
            timerange.getTz()
          );
          const startDayDelta = startDatetime.diff(
            moment.tz(moment(), timerange.getTz()).startOf("day"),
            "days"
          );
          const endDatetime = moment.tz(
            moment.unix(timerange.getEnd()).utc(),
            timerange.getTz()
          );
          const endDayDelta = endDatetime.diff(
            moment.tz(moment(), timerange.getTz()).startOf("day"),
            "days"
          );

          return {
            start: moment({
              h: startDatetime.hour(),
              m: startDatetime.minute(),
            }).add(startDayDelta, "d"),
            end: moment({ h: endDatetime.hour(), m: endDatetime.minute() }).add(
              endDayDelta,
              "d"
            ),
            uid: timerange.getId(),
            value: `${timerange.getId()}`
          };
        });

        this.setState({
          selectedIntervals: intervals,
        });
      })
      .catch((err) => {
        console.error(`error: ${err.code}, "${err.message}"`);
      });
  };

  render() {
    return (
      <WeekCalendar
        dayFormat={"ddd Do"}
        scaleUnit={30}
        cellHeight={20}
        numberOfDays={7}
        startTime={moment({ h: 8, m: 0 })}
        endTime={moment({ h: 22, m: 0 })}
        selectedIntervals={this.state.selectedIntervals}
        onIntervalSelect={this.handleSelect}
        onIntervalRemove={this.handleEventRemove}
        showModalCase={["edit"]}
      />
    );
  }
}
