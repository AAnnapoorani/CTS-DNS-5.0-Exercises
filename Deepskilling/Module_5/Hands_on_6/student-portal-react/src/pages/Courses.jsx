import { Link } from "react-router-dom";

function Courses() {
  const courses = [
    {
      id: 1,
      name: "Data Structures"
    },
    {
      id: 2,
      name: "Database Management Systems"
    },
    {
      id: 3,
      name: "Operating Systems"
    },
    {
      id: 4,
      name: "Computer Networks"
    },
    {
      id: 5,
      name: "Web Development"
    }
  ];

  return (
    <div className="page">
      <h2>Courses Page</h2>

      <ul>
        {courses.map((course) => (
          <li key={course.id}>
            <Link
              to={`/courses/${course.id}`}
            >
              {course.name}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Courses;