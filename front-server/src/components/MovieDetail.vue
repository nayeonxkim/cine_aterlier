<template>
  <div>
    <h1>Movie Detail, {{movieId}}</h1>
  </div>
</template>

<script>
export default {
  // Django로 axios 요청 보내기
  data(){
    return {
      movieId : this.$route.params.movieId
    }
  }
}
</script>

<style>

</style>