<template>
  <div>
    <div class="row">
      <div class="col-md-1"></div>
      <div class="col-md-10">
        <img :src="`https://image.tmdb.org/t/p/original${movieDetail.backdrop_path}`" alt="" width="80%" height="100%">
      </div>
      <div class="col-md-1"></div>
    </div>
    <div class="row pt-5 pb-5">
      <div class="col-md-1"></div>
      <div class="col-md-3">
        <img :src="`https://image.tmdb.org/t/p/original${movieDetail.poster_path}`" alt="">
      </div>
      <div class="col-md-1"></div>
      <div class="col-md-6">
        <h5 class="modal-title">{{movieDetail.title}}</h5>
        <p>{{movieDetail.release_date}}</p>
        <p v-for="genre in movieDetail.genres" :key="genre.id">{{genre.name}}</p>
        <p>{{movieDetail.runtime}}분</p>
        <p>{{movieDetail.popularity}}</p>
        <p>{{movieDetail.overview}}</p>
      </div>
      <div class="col-md-1"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  computed:{
    movieId(){
      return this.$route.params.movieId
    },
    movieDetail(){
      return this.$store.state.movieDetail
    }
  },
  data(){
    return {
      movieTrailer:null
    }
  },
  methods:{
    get_movie_detail(){
      return this.$store.dispatch('get_movie_detail', this.movieId)
    },

    getTrailer() {
      const searchWord = `${this.movieDetail.original_title} trailer`
      console.log(searchWord)
      axios
      .get('https://www.googleapis.com/youtube/v3/search', 
      {params :{
        part : 'snippet',
        type : 'video',
        key : 'AIzaSyDqAHcO6_gAszogUufo0gNwDR7WGjEl_Mo',
        q : searchWord
      }})
      .then((response) =>{
        this.movieTrailer = response.data.items
      })
    },
  },

  // created() {
  //   },
  mounted(){

    this.get_movie_detail()
  },
  // beforeUpdate(){
  //   this.getTrailer()

  // }
}
</script>

<style>
.image-container {
  width: 100%;
  height: 0;
  padding-bottom: 56.25%; 
  position: relative;
  overflow: hidden;
}

.image-container img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.image-container::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.7));
}
</style>
