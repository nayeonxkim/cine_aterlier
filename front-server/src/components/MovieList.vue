<template>
<div>
  <div class="row">
      <MovieItem 
      v-for="(movie, idx) in movieList" 
      :key="idx"
      :movie-item= movie 
      class="col-6 col-md-1 col-lg-1 mb-4" />
  </div>


</div>
</template>

<script>
import MovieItem from "@/components/MovieItem.vue";

export default {
  name: 'MovieList',
  components: {
    MovieItem,
  },
  computed: {
    movieList() {
      return this.$store.state.movieList;
    }
  },
  methods:{
    movieList_reset(){
      return this.$store.commit('MOVIELIST_RESET')
    }
  },
  destroyed(){
    this.movieList_reset()
  }
}
</script>

<style>
/* CSS styles for MovieList */
</style>