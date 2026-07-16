import { Link } from "react-router-dom";

function Header({ siteName }) {
  return (
    <header>
      <h1>{siteName}</h1>

      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>

          <li>
            <Link to="/courses">Courses</Link>
          </li>

          <li>
            <Link to="/profile">Profile</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;