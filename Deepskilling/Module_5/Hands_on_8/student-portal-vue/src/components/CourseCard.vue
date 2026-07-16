<script setup>
defineProps({
  name: String,
  code: String,
  credits: Number,
  grade: String
})
</script>

<template>
  <div class="card">
    <h3>{{ name }}</h3>
    <p><strong>Code:</strong> {{ code }}</p>
    <p><strong>Credits:</strong> {{ credits }}</p>
    <p><strong>Grade:</strong> {{ grade }}</p>
  </div>
</template>

<style scoped>
.card {
  background: white;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 15px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}
</style>