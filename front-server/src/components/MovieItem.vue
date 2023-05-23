<template>
  <div>
    <div @click="$router.push(`/movies/${movieItem.tmdb_id}`)">
      <!-- 포스터와 제목 보여주기 -->
      <img 
      :src="`https://image.tmdb.org/t/p/w500${movieItem.poster_path}`" 
      class="card-img-top" 
      style="width:330px; height:460px;"
      alt="Movie Poster">
      <p id="movie-title">{{movieItem.title}}</p>
      <hr id="movie-hr">
      <p>{{movieItem.release_date}}</p>
    </div>
  </div>
</template>

<script>


export default {
  name: 'MovieItem',
  props:{
    movieItem:Object
  },
  data() {
    return {
      selectedMovieId: null,
    };
  },
  computed: {
    movieList() {
      return this.$store.state.movieList
    }
  },
  methods: {
  }
}
</script>

<style>

@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');

img{
  margin-bottom: 2px;
}

#movie-title{
  font-size:25px !important;
}

div {
  font-family: 'Noto Sans KR', sans-serif;
}

.temp{
  width: 100%;
}

#movie-hr{
  
  height:3px; 
  border-color: #000000;
  margin-left : auto;
  margin-right : auto;
}
</style>