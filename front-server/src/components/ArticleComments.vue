<template>
  <div>
    <h1>Article Comments</h1>
    <div class="mt-5">
      <div v-for="comment in comments" :key="comment.id" class="card mt-3">
        <div class="card-body">
          <p>{{ comment.content }}</p>
          <p class="text-muted">작성자: {{ comment.author }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

</script>

<style>
</style>
