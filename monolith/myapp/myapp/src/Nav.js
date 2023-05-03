import { NavLink } from "react-router-dom";
function Nav() {
    return (
<nav className="navbar navbar-expand-lg navbar-light bg-light">
  <NavLink className="navbar-brand" to="/">PhilHub</NavLink>
  <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span className="navbar-toggler-icon"></span>
  </button>
  <div className="collapse navbar-collapse" id="navbarNav">
    <ul className="navbar-nav">
      <li className="nav-item active">
        <NavLink className="nav-link" to="/">Home</NavLink>
      </li>
      <li className="nav-item">
      <NavLink className="nav-link" aria-current="page" to="/searchworks">Search Papers</NavLink>
      </li>
      <li className="nav-item">
      <NavLink className="nav-link" aria-current="page" to="/searchworks/new">Upload</NavLink>
      </li>
      <li>
      <NavLink className="nav-link" aria-current="page" to="/noteslist">Notes</NavLink>
      </li>
      <li>
      <NavLink className="nav-link" aria-current="page" to="/profile">Profile</NavLink>
      </li>
      <li>
      <NavLink className="nav-link" aria-current="page" to="/contact">Contact</NavLink>
      </li>
      <li className="nav-item">
      <NavLink className="nav-link" aria-current="page" to="/login">Login</NavLink>
      </li>

    </ul>
  </div>
</nav>
    );
}
export default Nav;