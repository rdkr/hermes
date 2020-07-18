import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import { withRouter } from "react-router-dom";

import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";
// import FormHelperText from "@material-ui/core/FormHelperText";
// import MuiFormControl from "@material-ui/core/MuiFormControl";
import Select from "@material-ui/core/Select";
import TextField from "@material-ui/core/TextField";
import { FormControl } from "@material-ui/core";
import Slider from "@material-ui/core/Slider";
import Typography from "@material-ui/core/Typography";
import LinearProgress from "@material-ui/core/LinearProgress";

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

function EventPage({ msg, tz, events, currentEvent, hideCal }) {
  const [message, setMsg] = useState(msg);
  const [days, setDays] = useState(8);
  const [daysSlide, setDaysSlide] = useState(8);
  const [hours, setHours] = useState([20, 45]);
  const [hoursSlide, setHoursSlide] = useState([20, 45]);

  const [hideCalendar, setHiddenCalendar] = useState(hideCal);
  const [blurCalendar, setBlurredCalendar] = useState(false);

  const history = useHistory();
  const handleEventChange = (event) => {
    setBlurredCalendar(true);
    history.replace("/event/" + event.target.value);
  };

  return (
    <>
      <div style={{ float: "left" }}>
        <Typography variant={"h4"}>{message}</Typography>
        <div
          style={{
            display: events[0].name === "loading..." ? "none" : "",
          }}
        >
          <FormControl onSubmit={handleEventChange}>
            <InputLabel id="event-field-label">event</InputLabel>
            <Select
              labelId="event-field-label"
              value={currentEvent}
              onChange={handleEventChange}
            >
              {events.map((event) => (
                <MenuItem
                  key={event.name}
                  value={event.name}
                  hidden={
                    event.name === "please choose an event..." ? true : false
                  }
                  disabled={
                    event.name === "please choose an event..." ? true : false
                  }
                >
                  {event.name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          <FormControl>
            <TextField label="timezone" type="text" value={tz} disabled />
          </FormControl>
        </div>
      </div>
      <div
        style={{
          display: events[0].name.endsWith("...") ? "none" : "",
          float: "right",
        }}
      >
        <div>
          <div>
            <Typography id="range-slider" variant={"caption"}>
              date range
            </Typography>
            <Slider
              min={6}
              max={15}
              value={daysSlide}
              onChange={(event, value) => {
                setDaysSlide(value);
              }}
              onChangeCommitted={(event, value) => {
                setDays(value);
              }}
              valueLabelFormat={(value) => value - 1}
              valueLabelDisplay="auto"
              aria-labelledby="slider"
            />
          </div>

          <div>
            <Typography id="range-slider" variant={"caption"}>
              time ranges
            </Typography>
            <Slider
              min={0}
              max={48}
              value={hoursSlide}
              onChange={(event, value) => {
                setHoursSlide(value);
              }}
              onChangeCommitted={(event, value) => {
                setHours([value[0], value[1] + 1]);
              }}
              valueLabelFormat={valueToTime}
              valueLabelDisplay="auto"
              aria-labelledby="range-slider"
            />
          </div>
        </div>
      </div>
      <div>
        {blurCalendar ? <LinearProgress /> : null}
        <div
          style={{
            filter: blurCalendar ? "blur(5px)" : "none",
            display: events[0].name.endsWith("...") ? "none" : "",
          }}
        >
          <Calendar days={days} hours={hours} event={currentEvent} />
        </div>
      </div>
    </>
  );
}

export default withRouter(EventPage);
