import { useState, useEffect } from "react";

import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";

function App() {

  const [courses, setCourses] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");

  const [enrolledCount, setEnrolledCount] =
    useState(0);

  useEffect(() => {

    async function fetchCourses() {

      try {

        const response =
          await fetch(
            "https://jsonplaceholder.typicode.com/posts"
          );

        if (!response.ok) {
          throw new Error(
            "Failed to fetch courses"
          );
        }

        const data =
          await response.json();

        const courseNames = [
          "Data Structures",
          "Database Management Systems",
          "Web Development",
          "Operating Systems",
          "Computer Networks"
        ];

        const formattedCourses = data.slice(0, 5).map(
          (item, index) => ({
            id: index + 1,
            name: courseNames[index],
            code: `CS10${index + 1}`,
            credits: 4,
            grade: "A"
          })
        );

        setCourses(
          formattedCourses
        );

      }
      catch (err) {

        setError(
          err.message
        );

      }
      finally {

        setLoading(false);

      }
    }

    fetchCourses();

  }, []);

  const handleEnroll = () => {

    setEnrolledCount(
      enrolledCount + 1
    );

  };

  return (
    <>
      <Header siteName="Student Portal" />

      <main>

        <section className="hero">

          <h2>React Course Dashboard</h2>

          <h3>
            Enrolled Courses:
            {" "}
            {enrolledCount}
          </h3>

        </section>

        {loading && (
          <h2>Loading Courses...</h2>
        )}

        {error && (
          <h2>
            Error:
            {" "}
            {error}
          </h2>
        )}

        {!loading && !error && (

          <section className="courses">

            {courses.map(course => (

              <CourseCard
                key={course.id}
                name={course.name}
                code={course.code}
                credits={course.credits}
                grade={course.grade}
                onEnroll={
                  handleEnroll
                }
              />

            ))}

          </section>

        )}

        <StudentProfile />

      </main>

      <Footer />
    </>
  );
}

export default App;