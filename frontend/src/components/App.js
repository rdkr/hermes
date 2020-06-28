import React from "react";
import moment from "moment-timezone";
import StandardCalendar from "./StandardCalendar";

import Form from "./Form.js";

const { Login } = require("../proto/hermes_pb.js");
const { GatewayPromiseClient } = require("../proto/hermes_grpc_web_pb.js");

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
        "/hermes/?" + unescape(params.toString())
      );
    }

    let token = localStorage.getItem("token");
    if (token === null) {
      return this.setState({
        msg: `please log in from discord ($login)`,
      });
    }

    await this.setState({
      gateway: new GatewayPromiseClient(process.env.REACT_APP_BACKEND),
    });
    await this.login();
  }

  hideCalendar() {
    this.setState({hiddenCalendar: true})
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
              options: <Form tz={tz} events={listOfEvents} app={this} />,
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
            options: <Form tz={tz} events={listOfEvents} app={this} />,
            hiddenOptions: false,
          });
        }
      })
      .catch((err) => {
        console.log(`error: ${err.code}, "${err.message}"`);
        if (err.code === 2 && err.message === "invalid token") {
          return this.setState({
            msg: `please log in from discord ($login)`,
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

export default App;
