<template>
  <div>
    <div id="movie" @click="select_movie">
      <img :src="`https://image.tmdb.org/t/p/w500${selectedMovie.poster_path}`" alt="">
      <p>{{selectedMovie.title}}</p>
    </div>


  </div>
</template>

<script>
export default {
  name:'SelectedMovie',
  props:{
    selectedMovie:Object
  },
  methods:{
    select_movie(){
      this.$store.commit('SELECT_MOVIE', this.selectedMovie.tmdb_id)
    }
  }
}
</script>

<style>

</style>