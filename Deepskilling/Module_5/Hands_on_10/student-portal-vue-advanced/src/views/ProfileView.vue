<script setup>
import { useEnrollmentStore } from '../stores/enrollment'
import { storeToRefs } from 'pinia'

const store = useEnrollmentStore()

const {
    enrolledCourses,
    totalCourses
} = storeToRefs(store)

function clearEnrollments() {
    store.reset()
}
</script>

<template>
    <div>
        <h2>Student Profile</h2>

        <h3>Total Courses: {{ totalCourses }}</h3>

        <ul>
            <li v-for="course in enrolledCourses" :key="course.id">
                {{ course.title }}
            </li>
        </ul>

        <button @click="clearEnrollments">
            Reset Enrollments
        </button>
    </div>
</template>