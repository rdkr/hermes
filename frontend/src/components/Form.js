import React from "react";

class Form extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    event.preventDefault();
    this.props.app.redirect("event/" + event.target.value)
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <div className={"row"}>
          <div className={"column"}>
            <label htmlFor="eventField">event name</label>
            <select
              id="eventField"
              value={this.props.currentEvent}
              onChange={this.handleChange}
            >
              {this.props.events.map((event) => (
                <option
                  key={event.name}
                  value={event.name}
                  hidden={
                    event.name === "please choose an event..." ? true : false
                  }
                >
                  {event.name}
                </option>
              ))}
            </select>
          </div>

          <div className={"column"}>
            <label htmlFor="timezoneField">timezone</label>
            <input
              id="timezoneField"
              type="text"
              value={this.props.tz}
              disabled
            />
          </div>
        </div>
      </form>
    );
  }
}

export default Form;
