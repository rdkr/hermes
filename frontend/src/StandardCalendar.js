import React from 'react';
import moment from 'moment';
import WeekCalendar from 'react-week-calendar';

const { Login } = require("./proto/hermes_pb.js");
const { GatewayPromiseClient } = require("./proto/hermes_grpc_web_pb.js");

export default class StandardCalendar extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      lastUid: 0,
      selectedIntervals: []
    }
  }

  // async componentDidMount() {
  //   let search = window.location.search;
  //   let params = new URLSearchParams(search);
  //   let token = params.get("token");

  //   await this.setState({
  //     gateway: new GatewayPromiseClient("http://hermes.rdkr.uk:30007")
  //   })

  //   var login = new Login();
  //   login.setToken(token);

  //   this.state.gateway
  //     .getPlayer(login, {})
  //     .then((response) => {
  //       let name = response.getName();
  //       let tz = response.getTz();
  //       this.setState({
  //         msg: `welcome, ${name}! (${tz})`,
  //       });
  //     })
  //     .catch((err) => {
  //       console.log(`error: ${err.code}, "${err.message}"`);
  //       this.setState({
  //         msg: `invalid token :(`,
  //       });
  //     });
  // }

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
      scaleHeaderTitle = {"London"}
      dayFormat = {"ddd Do"}
      scaleUnit = {30}
      cellHeight = {20}
      numberOfDays= {14}
      startTime = {moment({h: 9, m: 0})}
      selectedIntervals = {this.state.selectedIntervals}
      onIntervalSelect = {this.handleSelect}
      onIntervalUpdate = {this.handleEventUpdate}
      onIntervalRemove = {this.handleEventRemove}
      showModalCase = {['edit']}
    />
  }
}
