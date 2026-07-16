<script setup>
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()
</script>

<template>
  <div class="container">

    <h2>Student Profile</h2>

    <p><strong>Name:</strong> Annapoorani</p>
    <p><strong>Department:</strong> CSE</p>
    <p><strong>Semester:</strong> 7</p>

    <hr>

    <h3>Enrolled Courses</h3>

    <ul>
      <li
        v-for="course in store.enrolledCourses"
        :key="course.id"
      >
        {{ course.name }}
        ({{ course.credits }} credits)
      </li>
    </ul>

    <h3>
      Total Credits:
      {{ store.totalCredits }}
    </h3>

  </div>
</template>