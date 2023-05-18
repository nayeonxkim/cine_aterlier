<template>
  <div>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <h1>Movie List</h1>
    <div class="row row-cols-3 row-cols-md-5 g-4">
      <MovieItem 
      v-for="movie in movieList"
      :key="movie.tmdb_id" 
      :movie-item="movie"
      />

    </div>

     <MovieDetail />


  </div>
</template>

<script>
import MovieItem from './MovieItem.vue'
import MovieDetail from './MovieDetail.vue'

export default {
  name: 'MovieList',
  components: {
    MovieItem,
    MovieDetail
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