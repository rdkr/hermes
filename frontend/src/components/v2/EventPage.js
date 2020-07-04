import React from "react";
import { Redirect, withRouter } from "react-router-dom";

import Typography from "@material-ui/core/Typography";
import Slider from "@material-ui/core/Slider";

import Calendar from "./Calendar";

class EventPage extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      days: 7,
      hours: [0, 49],
    };
  }

  render() {

    return (
      <>
        <Typography id="range-slider" gutterBottom>
          Temperature range
        </Typography>
        <Slider
        min={2}
        max={15}
          value={this.state.days}
          onChange={(event, value) => {this.setState({days: value})}}
          valueLabelDisplay="auto"
          aria-labelledby="slider"
          // getAriaValueText={valuetext}
        />
        <Slider
                min={2}
                max={49}
          value={this.state.hours}
          onChange={(event, value) => {this.setState({hours: value})}}
          valueLabelDisplay="auto"
          aria-labelledby="range-slider"
          // getAriaValueText={valuetext}
        />
        <Calendar days={this.state.days} hours={this.state.hours[1]} event={this.props.match.params.event} />
      </>
    );
  }
}

export default withRouter(EventPage);
