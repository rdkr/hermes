import React from 'react';
import moment from 'moment';
import WeekCalendar from 'react-week-calendar';

export default class StandardCalendar extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      lastUid: 0,
      selectedIntervals: []
    }
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

    const {EchoRequest, EchoResponse} = require('./proto/echo_pb.js');
    const {EchoServiceClient} = require('./proto/echo_grpc_web_pb.js');

    var echoService = new EchoServiceClient('http://localhost:8080');

    var request = new EchoRequest();
    request.setMessage('Hello World!');

    echoService.echo(request, {}, function(err, response) {
      console.log("o nooo")
    });

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
