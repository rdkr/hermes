import React from "react";
import moment from "moment-timezone";
import { Redirect, withRouter } from "react-router-dom";

import EventPage from "./EventPage";

const { Login } = require("../../proto/hermes_pb.js");
const { GatewayPromiseClient } = require("../../proto/hermes_grpc_web_pb.js");

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      gateway: new GatewayPromiseClient(process.env.REACT_APP_BACKEND),
      msg: "loading...",
      hiddenCalendar: true,
      events: [{"name": "loading..."}],
      currentEvent:"loading..."
    };
  }

  async componentDidMount() {
    await this.login();
  }

  componentDidUpdate(prevProps) {
    if (this.props.match.params !== prevProps.match.params) {
      this.setState({
        redirect: null,
      });
      this.login();
    }
  }

  redirect(query) {
    this.setState({
      hiddenCalendar: true,
      redirect: {
        pathname: "/" + query,
      },
    });
  }

  async login() {
    let token = localStorage.getItem("token");
    if (token === null) {
      this.redirect("login");
    }

    var login = new Login();
    login.setEvent(this.props.match.params.event);
    login.setToken(localStorage.getItem("token"));
    login.setTz(moment.tz.guess());

    this.state.gateway
      .getPlayer(login, {})
      .then((response) => {
        const name = response.getName();
        const tz = response.getTz();
        const events = response.getEventsList();

        this.setState({
          msg: `welcome, ${name}!`,
          tz: tz,
        });

        var found = false;
        for (const event of events) {
          if (event.getName() === this.props.match.params.event) {
            found = true;
            break;
          }
        }

        if (found) {
          let listOfEvents = events.map((event) => ({
            name: event.getName(),
          }));

          this.setState({
            events: listOfEvents,
            currentEvent: this.props.match.params.event,
            hiddenCalendar: false,
          });
        } else {
          let listOfEvents = [{ name: "please choose an event..." }];
          listOfEvents.push(
            ...events.map((event) => ({ name: event.getName() }))
          );
          this.setState({
            events: listOfEvents,
            currentEvent: listOfEvents[0].name,
            hiddenCalendar: false,
          });
        }
      })
      .catch((err) => {
        console.log(`error: ${err.code}, "${err.message}"`);
        if (err.code === 2 && err.message === "invalid token") {
          return this.setState({
            msg: `invalid token - please log in from discord ($login)`,
          });
        } else {
          this.setState({ msg: `server error :(` });
        }
      });
  }

  render() {
    if (this.state.redirect) {
      return <Redirect push to={this.state.redirect} />;
    }
    return (
      <div>
        <EventPage
          msg={this.state.msg}
          hideCal={this.state.hiddenCalendar}
          tz={this.state.tz}
          events={this.state.events}
          currentEvent={this.state.currentEvent}
          key={this.state.currentEvent}
        />
      </div>
    );
  }
}

export default withRouter(App);
