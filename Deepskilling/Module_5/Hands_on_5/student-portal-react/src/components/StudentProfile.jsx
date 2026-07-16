import { useState } from "react";

function StudentProfile() {

  const [student, setStudent] = useState({
    name: "",
    email: ""
  });

  const handleChange = (e) => {

    setStudent({
      ...student,
      [e.target.name]: e.target.value
    });

  };

  return (
    <div className="profile-form">

      <h2>Student Profile</h2>

      <input
        type="text"
        name="name"
        placeholder="Enter Name"
        value={student.name}
        onChange={handleChange}
      />

      <input
        type="email"
        name="email"
        placeholder="Enter Email"
        value={student.email}
        onChange={handleChange}
      />

      <div className="profile-preview">

        <h3>Profile Preview</h3>

        <p>Name: {student.name}</p>

        <p>Email: {student.email}</p>

      </div>

    </div>
  );
}

export default StudentProfile;