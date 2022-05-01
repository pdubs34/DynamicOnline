import React from "react";
import ReactDOM from "react-dom/client";
import LoginManager from "./LoginManager";
import reportWebVitals from "./reportWebVitals";
import { BrowserRouter, Routes, Route, Link} from "react-router-dom";
import Layout from "./Layout";
import Home from "./TesterRoutes/Home";
import NoPage from "./TesterRoutes/NoPage";
import NewLogin from "./Controller/NewLogin";

export default function Program() {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route exact path="/LoginManager" element={<LoginManager />} />
          <Route exact path="/NewLogin" element={<NewLogin />} />
          <Route exact path="*" element={<NoPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Program />);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
