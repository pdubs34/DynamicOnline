import React, { Fragment } from "react";
import ReactDOM from "react-dom/client";

import "./index.css";
import LoginManager from "./Controllers/LoginManager";

const root = ReactDOM.createRoot(document.getElementById("root"))
root.render(
  <Fragment>
    <LoginManager />
  </Fragment>,
);

