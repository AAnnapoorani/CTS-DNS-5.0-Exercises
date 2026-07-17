<script setup>
import { ref, onMounted } from 'vue'
import { getAllCourses } from '../api/courseApi'
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

const courses = ref([])

const customTitles = [
    'Data Structures',
    'Database Management Systems',
    'Operating Systems',
    'Computer Networks',
    'Web Development'
]

onMounted(async () => {
    try {
        const data = await getAllCourses()

        courses.value = data.slice(0, 5).map((item, index) => ({
            id: item.id,
            title: customTitles[index]
        }))
    } catch (error) {
        alert(error.message)
    }
})

async function enroll(course) {
    try {
        await store.fetchAndEnroll(course)
        alert(`${course.title} enrolled successfully!`)
    } catch (error) {
        alert(error.message)
    }
}
</script>

<template>
    <div class="courses-container">
        <h2>Available Courses</h2>

        <div v-for="course in courses" :key="course.id" class="course-card">
            <h3>{{ course.title }}</h3>

            <p>Course ID: {{ course.id }}</p>

            <button @click="enroll(course)">
                Enroll
            </button>
        </div>
    </div>
</template>

<style scoped>
.courses-container {
    padding: 20px;
}

.course-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 15px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

button {
    background-color: #2c3e50;
    color: white;
    border: none;
    padding: 8px 15px;
    cursor: pointer;
    border-radius: 5px;
}

button:hover {
    background-color: #34495e;
}
</style>