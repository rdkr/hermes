import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import * as serviceWorker from "./serviceWorker";

import CssBaseline from "@material-ui/core/CssBaseline";
import { ThemeProvider, createMuiTheme } from "@material-ui/core/styles";
import Container from '@material-ui/core/Container';

import "./index.css";

import Login from "./components/login/Login";
import App from "./components/event/App";

import purple from '@material-ui/core/colors/purple';

const darkTheme = createMuiTheme({
  palette: {
    type: "dark",
    primary: {
      main: purple[500],
    }
  },
  // spacing: 60
});

const NoMatch = () => {
  return <h1>page not found</h1>;
};

ReactDOM.render(
  <React.StrictMode>
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Container component="main">
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
            <Route component={NoMatch} />
          </Switch>
        </BrowserRouter>
      </Container>
    </ThemeProvider>
  </React.StrictMode>,
  document.getElementById("root")
);

serviceWorker.unregister();
