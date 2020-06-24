import React from "react";
import ReactDOM from "react-dom";
import moment from "moment-timezone";

import "./index.css";
import * as serviceWorker from "./serviceWorker";
import StandardCalendar from "./StandardCalendar";

const { Login } = require("./proto/hermes_pb.js");
const { GatewayPromiseClient } = require("./proto/hermes_grpc_web_pb.js");

class NameForm extends React.Component {
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
        "/hermes/" + "?" + unescape(params.toString())
      );
    } else {
      window.history.pushState(
        {},
        document.title,
        "/hermes/" + "?" + unescape(params.toString())
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

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      msg: "loading...",
      calendar: "",
      hiddenOptions: true,
      hiddenCalendar: true,
    };
  }

  async componentDidMount() {
    let search = window.location.search;
    let params = new URLSearchParams(search);
    let urlToken = params.get("token");

    if (urlToken != null) {
      localStorage.setItem("token", urlToken);
      params.delete("token");
      window.history.replaceState(
        {},
        document.title,
        "/hermes/" + "?" + unescape(params.toString())
      );
    }

    let token = localStorage.getItem("token");
    if (token === null) {
      return this.setState({
        msg: `please log in from discord (!login)`,
      });
    }

    await this.setState({
      gateway: new GatewayPromiseClient(process.env.REACT_APP_BACKEND),
    });
    await this.login();
  }

  async login() {
    let search = window.location.search;
    let params = new URLSearchParams(search);
    let eventName = params.get("event");

    var login = new Login();
    login.setEvent(eventName);
    login.setToken(localStorage.getItem("token"));
    login.setTz(moment.tz.guess());

    this.state.gateway
      .getPlayer(login, {})
      .then((response) => {
        const name = response.getName();
        const tz = response.getTz();
        const events = response.getEventsList();

        var found = false;

        for (const event of events) {
          if (event.getName() === eventName) {
            let listOfEvents = events.map((event) => ({
              name: event.getName(),
            }));

            this.setState({
              msg: `welcome, ${name}!`,
              options: <NameForm tz={tz} events={listOfEvents} app={this} />,
              calendar: <StandardCalendar tz={tz} event={eventName} />,
              hiddenOptions: false,
              hiddenCalendar: false,
            });

            found = true;
            break;
          }
        }
        if (!found) {
          let listOfEvents = [{ name: "please choose an event..." }];
          listOfEvents.push(
            ...events.map((event) => ({ name: event.getName() }))
          );
          this.setState({
            msg: `welcome, ${name}!`,
            options: <NameForm tz={tz} events={listOfEvents} app={this} />,
            hiddenOptions: false,
          });
        }
      })
      .catch((err) => {
        console.log(`error: ${err.code}, "${err.message}"`);
        if (err.code === 2 && err.message === "invalid token") {
          return this.setState({
            msg: `please log in from discord (!login)`,
          });
        } else {
          this.setState({ msg: `server error :(` });
        }
      });
  }

  render() {
    return (
      <div>
        <div className={"container"}>
          <div className={"row"}>
            <div className={"column"}>
              <h1>{this.state.msg}</h1>
            </div>
          </div>

          {this.state.options}

          <div
            className={"row"}
            style={this.state.hiddenCalendar ? { visibility: "hidden" } : {}}
          >
            <div className={"column"}>{this.state.calendar}</div>
          </div>
        </div>
      </div>
    );
  }
}

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
