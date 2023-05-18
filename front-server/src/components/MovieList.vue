<template>
  <div>
    <h1>Movie List</h1>
    <MovieItem 
    v-for="movie in movieList"
    :key="movie.tmdb_id" 
    :movie-item="movie"
     />

  </div>
</template>

<script>
import MovieItem from './MovieItem.vue'

export default {
  name: 'MovieList',
  components: {
    MovieItem
  },
  // store에서 모든 영화 정보 가져오기
  methods:{
    get_movie_list(){
      this.$store.dispatch('get_movie_list')
    },

  },
  computed:{
    movieList(){
      return this.$store.state.movieList
    }
  },
  created(){
    this.get_movie_list()
  }

}
</script>

<style>

</style>