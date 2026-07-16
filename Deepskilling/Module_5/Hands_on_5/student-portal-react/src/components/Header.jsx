function Header(props) {
  return (
    <header>
      <h1>{props.siteName}</h1>

      <nav>
        <ul>
          <li>Home</li>
          <li>Courses</li>
          <li>Profile</li>
          <li>Grades</li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;