import React from 'react';
import moment from 'moment-timezone';
import WeekCalendar from 'react-week-calendar';

const { Login } = require("./proto/hermes_pb.js");
const { GatewayPromiseClient } = require("./proto/hermes_grpc_web_pb.js");

export default class StandardCalendar extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      lastUid: 4,
      selectedIntervals: [
        // {
        //   uid: 1,
        //   start: moment({h: 10, m: 5}),
        //   end: moment({h: 12, m: 5}),
        //   value: "Booked by Smith"
        // },
        // {
        //   uid: 2,
        //   start: moment({h: 13, m: 0}).add(2,'d'),
        //   end: moment({h: 13, m: 45}).add(2,'d'),
        //   value: "Closed"
        // },
        // {
        //   uid: 3,
        //   start: moment({h: 11, m: 0}),
        //   end: moment({h: 14, m: 0}),
        //   value: "Reserved by White"
        // },
      ]
    }
  }

  async componentDidMount() {
    let search = window.location.search;
    let params = new URLSearchParams(search);
    let token = params.get("token");
    let event = params.get("event");

    await this.setState({
      gateway: new GatewayPromiseClient("https://hermes-gateway.rdkr.uk")
      // gateway: new GatewayPromiseClient("http://localhost:8080")
    })

    var login = new Login();
    login.setToken(token);
    login.setEventname(event);

    this.state.gateway
      .getTimeranges(login, {})
      .then((response) => {
        const selectedIntervals = this.state.selectedIntervals;

        const intervals = response.getTimerangesList().map( (timerange) => {
          const startDatetime = moment.tz(moment.unix(timerange.getStart()).utc(), timerange.getTz())
          const startDayDelta = startDatetime.diff(moment.now(), 'days', true)
          const endDatetime = moment.tz(moment.unix(timerange.getEnd()).utc(), timerange.getTz())
          const endDayDelta = endDatetime.diff(moment.now(), 'days', true)
          return {
            start: moment({h: startDatetime.hour(), m: startDatetime.minute()}).add(startDayDelta,'d'),
            end: moment({h: endDatetime.hour(), m: endDatetime.minute()}).add(endDayDelta,'d'),
            uid: timerange.getId()
          }
        });

        console.log(intervals)
        this.setState({
          selectedIntervals: selectedIntervals.concat(intervals),
        })

      })
      .catch((err) => {
        console.log(`error: ${err.code}, "${err.message}"`);
      });
  }

  handleEventRemove = (event) => {
    const {selectedIntervals} = this.state;
    const index = selectedIntervals.findIndex((interval) => interval.uid === event.uid);
    if (index > -1) {
      selectedIntervals.splice(index, 1);
      this.setState({selectedIntervals});
    }

  }

  handleEventUpdate = (event) => {
    const {selectedIntervals} = this.state;
    const index = selectedIntervals.findIndex((interval) => interval.uid === event.uid);
    if (index > -1) {
      selectedIntervals[index] = event;
      this.setState({selectedIntervals});
    }
  }

  handleSelect = (newIntervals) => {
    const {lastUid, selectedIntervals} = this.state;
    const intervals = newIntervals.map( (interval, index) => {
      return {
        ...interval,
        uid: lastUid + index
      }
    });

    console.log(intervals)

    this.setState({
      selectedIntervals: selectedIntervals.concat(intervals),
      lastUid: lastUid + newIntervals.length
    })
  }

  render() {
    return <WeekCalendar
      dayFormat = {"ddd Do"}
      scaleUnit = {30}
      cellHeight = {20}
      numberOfDays= {7}
      startTime = {moment({h: 8, m: 0})}
      endTime = {moment({h: 22, m: 0})}
      selectedIntervals = {this.state.selectedIntervals}
      // onIntervalSelect = {this.handleSelect}
      // onIntervalUpdate = {this.handleEventUpdate}
      // onIntervalRemove = {this.handleEventRemove}
      showModalCase = {['edit']}
    />
  }
}
