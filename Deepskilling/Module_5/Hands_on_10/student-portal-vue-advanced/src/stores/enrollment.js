import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { enrollStudent } from '../api/courseApi'

export const useEnrollmentStore = defineStore('enrollment', () => {
  const enrolledCourses = ref([])

  const totalCourses = computed(() => enrolledCourses.value.length)

  async function fetchAndEnroll(course) {
    await enrollStudent(1, course.id)
    enrolledCourses.value.push(course)
  }

  function reset() {
    enrolledCourses.value = []
  }

  return {
    enrolledCourses,
    totalCourses,
    fetchAndEnroll,
    reset
  }
})