import React from "react";

import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";
// import FormHelperText from "@material-ui/core/FormHelperText";
// import MuiFormControl from "@material-ui/core/MuiFormControl";
import Select from "@material-ui/core/Select";
import TextField from "@material-ui/core/TextField";
import { FormControl } from '@material-ui/core';
import Slider from "@material-ui/core/Slider";
import Typography from "@material-ui/core/Typography";

// import { makeStyles } from '@material-ui/core/styles';
// const useStyles = makeStyles((theme) => ({
//   formControl: {
//     margin: theme.spacing(1),
//     minWidth: 120,
//   },
//   selectEmpty: {
//     marginTop: theme.spacing(2),
//   },
// }));

class Form extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    event.preventDefault();
    this.props.app.redirect("event/" + event.target.value);
  }

  render() {
    return (
      <>
      <FormControl onSubmit={this.handleSubmit} >
        <InputLabel id="event-field-label">event name</InputLabel>
        <Select
          labelId="event-field-label"
          value={this.props.currentEvent}
          onChange={this.handleChange}
          autoWidth={true}

        >
          {this.props.events.map((event) => (
            <MenuItem
              key={event.name}
              value={event.name}
              hidden={event.name === "please choose an event..." ? true : false}
            >
              {event.name}
            </MenuItem>
          ))}
        </Select>
      </FormControl>

      <FormControl>
        <TextField
          label="timezone"
          type="text"
          value={this.props.tz}
          disabled
        />
      </FormControl>

      </>
    );
  }
}

export default Form;
