<template>
  <div>
    <div class="image-container">
      <img :src="`https://image.tmdb.org/t/p/w500${movieDetail.backdrop_path}`" alt="" width="80%" height="80%">
    </div>

      <h5 class="modal-title">{{movieDetail.title}}</h5>
      <img :src="`https://image.tmdb.org/t/p/w500${movieDetail.poster_path}`" alt="">
      <p>{{movieDetail.release_date}}</p>
      <p v-for="genre in movieDetail.genres"
      :key="genre.id">{{genre.name}}</p>
      <p>{{movieDetail.runtime}}분</p>
      <p>{{movieDetail.popularity}}</p>
      <p>{{movieDetail.overview}}</p>
      <p>{{movieDetail}}</p> 
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
  padding-bottom: 56.25%; /* 이미지 비율에 따라 조정 */
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
  filter: grayscale(70%);
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