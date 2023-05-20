<template>
  <div>
    <div class="card" @click="toDetail">
      <img :src="`https://image.tmdb.org/t/p/w500${movieItem.poster_path}`" class="card-img-top" alt="Movie Poster">
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieItem',
  props:{
    movieItem:Object
  },
  computed: {
    movieList() {
      return this.$store.state.movieList
    }
  },
  methods:{
    toDetail(){
      this.$router.push({name:'movie-detail', params :{movieId:this.movieItem.tmdb_id}})
    }
  }
}
</script>

<style>
/* CSS styles for MovieItem */
</style>