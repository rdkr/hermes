import React from "react";
import { withRouter } from "react-router-dom";

import LinearProgress from "@material-ui/core/LinearProgress";
import Typography from "@material-ui/core/Typography";
import Slider from "@material-ui/core/Slider";
import Box from "@material-ui/core/Box";
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormHelperText from '@material-ui/core/FormHelperText';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';

import Calendar from "./Calendar";

function valueToTime(value) {
  let h = Math.floor(value / 2);
  if (h === 24) {
    h = "00";
  } else if (h < 10) {
    h = `0${h}`;
  }
  let m = ((value / 2) % 1) * 60;
  if (m !== 30) {
    m = "00";
  }
  return `${h}${m}`;
}

class EventPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      days: 8,
      daysSlide: 8,
      hours: [20, 45],
      hoursSlide: [20, 45],
    };
  }

  render() {
    return (
      <>     
        <div style={{ width: '100%' }}>
          <Typography id="range-slider" variant={'caption'}>
            date range
          </Typography>
          <Slider
            min={6}
            max={15}
            value={this.state.daysSlide}
            onChange={(event, value) => {
              this.setState({ daysSlide: value });
            }}
            onChangeCommitted={(event, value) => {
              this.setState({ days: value });
            }}
            valueLabelFormat={(value) => value - 1}
            valueLabelDisplay="auto"
            aria-labelledby="slider"
          />
          <Typography id="range-slider" variant={'caption'}>
            time range
          </Typography>
          <Slider
            min={0}
            max={48}
            value={this.state.hoursSlide}
            onChange={(event, value) => {
              this.setState({ hoursSlide: value });
            }}
            onChangeCommitted={(event, value) => {
              this.setState({ hours: [value[0], value[1] + 1] });
            }}
            valueLabelFormat={valueToTime}
            valueLabelDisplay="auto"
            aria-labelledby="range-slider"
            // getAriaValueText={valuetext}
          />
                  <Calendar
          days={this.state.days}
          hours={this.state.hours}
          event={this.props.match.params.event}
        />
        </div>
      </>
    );
  }
}

export default withRouter(EventPage);
