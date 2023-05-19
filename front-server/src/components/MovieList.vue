<template>
  <div>
    <h1>MovieList</h1>
    <ul>
      <li v-for="movie in movieList" :key="movie.id"></li>
    </ul>
    <MovieItem />
  </div>
</template>

<script>
import MovieItem from "@/components/MovieItem.vue";

export default {
  name: 'MovieList',
  components: {
    MovieItem
  },
  computed: {
    movieList() {
      return this.$store.state.movieList;
    }
  }
}
</script>

<style>
/* CSS styles for MovieList */
</style>