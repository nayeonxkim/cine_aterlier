<template>
  <div>
    <div class="card" v-for="movie in movieList" :key="movie.id">
      <img :src="movie.poster" class="card-img-top" alt="Movie Poster">
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieItem',
  computed: {
    movieList() {
      return this.$store.state.movieList
    }
  }
}
</script>

<style>
/* CSS styles for MovieItem */
</style>