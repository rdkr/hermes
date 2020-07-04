import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import "./index.css";
import * as serviceWorker from "./serviceWorker";

import Login from "./components/Login.js";
import App from "./components/App.js";

import CssBaseline from "@material-ui/core/CssBaseline";

import EventPage from "./components/EventPage";

import { ThemeProvider, createMuiTheme } from "@material-ui/core/styles";

const darkTheme = createMuiTheme({
  palette: {
    type: "dark",
  },
});

const NoMatch = () => {  return (<h1>page not found</h1>);};

ReactDOM.render(
  <React.StrictMode>
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <BrowserRouter>
        <Switch>
          <Route exact path="/login">
            <Login />
          </Route>
          <Route exact path="/">
            <App />
          </Route>
          <Route exact path="/event">
            <App />
          </Route>
          <Route path="/event/:event+">
            <App />
          </Route>
          <Route exact path="/v2">
          <EventPage />
          </Route>
          <Route path="/v2/:event+">
            <EventPage />
          </Route>
          <Route component={NoMatch} />
        </Switch>
      </BrowserRouter>
    </ThemeProvider>
  </React.StrictMode>,
  document.getElementById("root")
);

serviceWorker.unregister();
