import React from "react";
import { Redirect, withRouter } from "react-router-dom";

class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      redirect: null,
    };
  }

  async componentDidMount() {
    let search = window.location.search;
    let params = new URLSearchParams(search);
    let urlToken = params.get("token");

    if (urlToken != null) {
      localStorage.setItem("token", urlToken);
    }

    let token = localStorage.getItem("token");
    if (token === null) {
      return this.setState({
        msg: `no token - please log in from discord ($login)`,
      });
    }
    this.setState({ redirect: { pathname: "/event" } });
  }

  render() {
    if (this.state.redirect) {
      return <Redirect push to={this.state.redirect} />;
    }
    return (
      <div>
        <div className={"container"}>
          <div className={"row"}>
            <div className={"column"}>
              <h1>{this.state.msg}</h1>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default withRouter(Login);
