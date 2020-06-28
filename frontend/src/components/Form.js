import React from "react";

class Form extends React.Component {
  constructor(props) {
    super(props);

    let search = window.location.search;
    let params = new URLSearchParams(search);

    if (this.props.events[0] === "please choose an event...") {
      this.state = { defaultEvent: "please choose an event..." };
    } else {
      this.state = { defaultEvent: params.get("event") };
    }
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    event.preventDefault();
    let params = new URLSearchParams(window.location.search);
    params.set("event", event.target.value);
    if (this.state.defaultEvent === "please choose an event...") {
      window.history.pushState(
        {},
        document.title,
        "/hermes/?" + unescape(params.toString())
      );
    } else {
      window.history.pushState(
        {},
        document.title,
        "/hermes/?" + unescape(params.toString())
      );
    }
    this.props.app.login();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <div className={"row"}>
          <div className={"column"}>
            <label htmlFor="eventField">event name</label>
            <select
              id="eventField"
              defaultValue={this.state.defaultEvent}
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
