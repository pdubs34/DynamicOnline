import { Outlet, Link } from "react-router-dom";

const Layout = () => {
  return (
    <>
      <div className="HomeLayout">
      <Link to="/">Home</Link>
      
      </div>
      <Link to="/LoginManager">Login</Link>
      <Outlet />
    </>
  );
};

export default Layout;
