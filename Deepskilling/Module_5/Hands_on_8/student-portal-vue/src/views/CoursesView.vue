<script setup>
import { ref, computed } from 'vue'
import CourseCard from '../components/CourseCard.vue'
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

const searchTerm = ref('')

const courses = ref([
  {
    id: 1,
    name: 'Data Structures',
    code: 'CS201',
    credits: 4,
    grade: 'A'
  },
  {
    id: 2,
    name: 'Database Management Systems',
    code: 'CS202',
    credits: 3,
    grade: 'A+'
  },
  {
    id: 3,
    name: 'Operating Systems',
    code: 'CS203',
    credits: 4,
    grade: 'B+'
  },
  {
    id: 4,
    name: 'Computer Networks',
    code: 'CS204',
    credits: 3,
    grade: 'A'
  },
  {
    id: 5,
    name: 'Web Development',
    code: 'CS205',
    credits: 4,
    grade: 'A+'
  }
])

const filteredCourses = computed(() =>
  courses.value.filter(course =>
    course.name
      .toLowerCase()
      .includes(searchTerm.value.toLowerCase())
  )
)

function enrollCourse(course) {
  store.enroll(course)
}
</script>

<template>
  <div class="container">
    <h2>Available Courses</h2>

    <input
      v-model="searchTerm"
      type="text"
      placeholder="Search Courses"
      class="search-box"
    />

    <div
      v-for="course in filteredCourses"
      :key="course.id"
      class="course-wrapper"
    >
      <CourseCard
        :name="course.name"
        :code="course.code"
        :credits="course.credits"
        :grade="course.grade"
      />

      <button
        class="enroll-btn"
        @click="enrollCourse(course)"
      >
        Enroll
      </button>
    </div>
  </div>
</template>

<style scoped>
.container {
  padding: 20px;
}

.search-box {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  font-size: 16px;
}

.course-wrapper {
  margin-bottom: 20px;
}

.enroll-btn {
  background: #2c3e90;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
}

.enroll-btn:hover {
  background: #1f2d6b;
}
</style>