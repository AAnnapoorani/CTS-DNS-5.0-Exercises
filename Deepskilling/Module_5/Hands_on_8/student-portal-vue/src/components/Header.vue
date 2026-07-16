<script setup>
import { RouterLink } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()
</script>

<template>
  <header class="header">
    <h1>Student Portal</h1>

    <nav>
      <RouterLink to="/">Home</RouterLink>

      <RouterLink to="/courses">
        Courses
      </RouterLink>

      <RouterLink to="/profile">
        Profile
      </RouterLink>
    </nav>

    <p>
      Enrolled Courses:
      {{ store.enrolledCourses.length }}
    </p>
  </header>
</template>

<style scoped>
.header {
  background: #2c3e90;
  color: white;
  text-align: center;
  padding: 20px;
}

nav {
  margin: 10px 0;
}

a {
  color: white;
  margin: 0 15px;
  text-decoration: none;
}
</style>