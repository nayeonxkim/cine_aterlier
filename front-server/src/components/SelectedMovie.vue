<template>
  <div>
    <div id="movie" @click="select_movie"  :class="{ 'selected-movie': selected }">
      <img :src="`https://image.tmdb.org/t/p/w500${selectedMovie.poster_path}`" style="width: 70%; height: 50%px;" alt="">
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
  data() {
    return {
      selected: false
    }
  },
  methods:{
    select_movie(){
      this.$store.commit('SELECT_MOVIE', this.selectedMovie.tmdb_id)
    }
  }
}
</script>

<style>
.selected-movie {
  border: 2px solid red;
  padding: 10px;
  background-color: red;
}
</style>