import React from "react";
import ReactDOM from "react-dom";
import moment from "moment-timezone";

import "./index.css";
import "react-week-calendar/dist/style.css";
import * as serviceWorker from "./serviceWorker";
import StandardCalendar from "./StandardCalendar";

const { Login } = require("./proto/hermes_pb.js");
const { GatewayPromiseClient } = require("./proto/hermes_grpc_web_pb.js");

class NameForm extends React.Component {
  constructor(props) {
    super(props);

    let search = window.location.search;
    let params = new URLSearchParams(search);

    this.state = { value: params.get("event") };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ value: event.target.value });
  }
  handleSubmit(event) {
    let currentUrlParams = new URLSearchParams(window.location.search);
    currentUrlParams.set("event", this.state.value);
    window.location.href = window.location.pathname + "?" + unescape(currentUrlParams.toString())
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          <input
            type="text"
            value={this.state.value}
            onChange={this.handleChange}
          />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      msg: "loading...",
      msg2: "",
      calendar: "",
      hiddenOptions: true,
      hiddenCalendar: true
    };
  }

  async componentDidMount() {
    let search = window.location.search;
    let params = new URLSearchParams(search);
    let token = params.get("token");
    let event = params.get("event");

    await this.setState({
      gateway: new GatewayPromiseClient(process.env.REACT_APP_BACKEND)
    })

    var login = new Login();
    login.setToken(token)
    login.setEvent(event)
    login.setTz(moment.tz.guess())

    this.state.gateway
      .getPlayer(login, {})
      .then((response) => {
        const name = response.getName();
        const tz = response.getTz();

        this.setState({
          msg: `welcome, ${name}!`,
          msg2: `tz: ${tz}`,
          calendar: <StandardCalendar tz={tz}/>,
          hiddenOptions: false,
          hiddenCalendar: false,
        });
      })
      .catch((err) => {
        console.log(`error: ${err.code}, "${err.message}"`);
        if (err.code === 2) {
          this.setState({
            msg: `${err.message} :(`,
          });
          if (err.message == "invalid event") {
            this.setState({
              hiddenOptions: false
            });
          }
        } else {
          this.setState({ msg: `server error :(` });
        }
      });
  }

  render() {
    return (
      <div>
        <h1>{this.state.msg}</h1>
        <div style={this.state.hiddenOptions ? { visibility: "hidden" } : {}} className={"row"}>
          <div className={"column"}>set the event in the format server-name/channel-name:</div>
          <div className={"column"}><NameForm /></div>
          <div className={"column"}>{this.state.msg2}</div>
        </div>
        <div style={this.state.hiddenCalendar ? { visibility: "hidden" } : {}}>
          {this.state.calendar}
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
