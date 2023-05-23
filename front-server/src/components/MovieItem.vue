<template>
  <div>
    <div @click="$router.push(`/movies/${movieItem.tmdb_id}`)">
      <!-- 포스터와 제목 보여주기 -->
      <div class="container">
      <img :src="`https://image.tmdb.org/t/p/w500${movieItem.poster_path}`"
      alt="Avatar"
      style="width:321px; height:460px; ">
      <div class="overlay">
        <h5><b>{{ movieItem.title }}</b></h5> 
        <p>{{ movieItem.release_date }}</p> 
      </div>
    </div>
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
* {box-sizing: border-box}

/* Container needed to position the overlay. Adjust the width as needed */
.container {
  position: relative;
  width: 50%;
  max-width: 300px;
}

/* Make the image to responsive */
.image {
  display: block;
  width: 100%;
  height: auto;
}

/* The overlay effect - lays on top of the container and over the image */
.overlay {
  position: absolute; 
  bottom: 0; 
  background: rgb(0, 0, 0);
  background: rgba(0, 0, 0, 0.8); /* Black see-through */
  color: #f1f1f1; 
  width: 100%;
  transition: .5s ease;
  opacity:0;
  color: white;
  font-size: 20px;
  padding: 20px;
  text-align: center;
}

/* When you mouse over the container, fade in the overlay title */
.container:hover .overlay {
  opacity: 1;
}

/* @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');

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
} */
</style>