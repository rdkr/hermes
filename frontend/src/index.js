import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import "react-week-calendar/dist/style.css";
import * as serviceWorker from "./serviceWorker";
import StandardCalendar from "./StandardCalendar";

const { Login } = require("./proto/hermes_pb.js");
const { GatewayPromiseClient } = require("./proto/hermes_grpc_web_pb.js");

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { msg: "", msg2: "", hidden: true };
  }

  async componentDidMount() {
    let search = window.location.search;
    let params = new URLSearchParams(search);
    let token = params.get("token");
    let event = params.get("event");

    await this.setState({
      gateway: new GatewayPromiseClient("https://hermes-gateway.rdkr.uk")
      // gateway: new GatewayPromiseClient("http://localhost:8080")
    })

    var login = new Login();
    login.setToken(token);

    this.state.gateway
      .getPlayer(login, {})
      .then((response) => {
        let name = response.getName();
        let tz = response.getTz();
        this.setState({
          msg: `welcome, ${name}!`,
          msg2: `tz: ${tz}, event: ${event}`,
          hidden: false
        });
      })
      .catch((err) => {
        console.log(`error: ${err.code}, "${err.message}"`);
        if (err.code === 2) {
          this.setState({msg: `invalid token :(`});
        } else {
          this.setState({msg: `server error :(`,});
        }
      });
  }

  render() {
    return (
      <div>
        <h1>{this.state.msg}</h1>
        <h2>{this.state.msg2}</h2>
        <div style={this.state.hidden ? { visibility : "hidden" } : {}}><StandardCalendar/></div>
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
