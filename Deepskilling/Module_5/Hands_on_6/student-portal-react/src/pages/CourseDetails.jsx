import { useParams } from "react-router-dom";

function CourseDetails() {
  const { id } = useParams();

  return (
    <div className="page">
      <h2>Course Details</h2>

      <p>
        Viewing details for Course ID:
        <strong> {id}</strong>
      </p>

      <p>
        This page demonstrates dynamic routing
        using React Router useParams().
      </p>
    </div>
  );
}

export default CourseDetails;