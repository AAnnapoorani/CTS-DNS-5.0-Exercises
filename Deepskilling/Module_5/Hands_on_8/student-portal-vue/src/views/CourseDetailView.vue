<script setup>
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const courseId = route.params.id

function enrollCourse() {
  router.push('/profile')
}
</script>

<template>
  <div class="container">
    <h2>Course Detail</h2>

    <p>Selected Course ID: {{ courseId }}</p>

    <button @click="enrollCourse">
      Enroll
    </button>
  </div>
</template>