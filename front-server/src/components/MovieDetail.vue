<template>
  <div>
    <div class="row">
      <div class="col-md-1"></div>
      <div class="col-md-10">
        <img :src="`https://image.tmdb.org/t/p/original${movieDetail.backdrop_path}`" alt="" width="80%" height="100%">
      </div>
      <div class="col-md-1"></div>
    </div>
    <div class="row pt-5 pb-5 pl-0">
      <div class="col-md-1"></div>
      <div class="col-md-3 pl-0">
        <img :src="`https://image.tmdb.org/t/p/original${movieDetail.poster_path}`" alt="">
      </div>
      <div class="col-md-6">
        <div class="movie-detail-infomation">
          <h5 class="moviedetail-title">{{ movieDetail.title }}   {{ movieDetail.original_title }}</h5>
          <span class="star">
            ★★★★★
            <span>★★★★★</span>
            <span>{{ movieDetail.vote_average }}</span>
            <input type="range" oninput="drawStar(this)" value="1" step="1" min="0" max="10">
          </span>
          <div class="genres-container">
            <span v-for="genre in movieDetail.genres" :key="genre.id" class="genre">{{ genre.name }}</span>
            <p>{{ movieDetail.runtime }}분</p>
          </div>
          <!-- <p>{{ movieDetail.popularity }}</p> -->
          <p>{{ movieDetail.release_date }}</p>
          <p>{{ movieDetail.overview }}</p>
          <!-- <p>{{movieDetail}}</p> -->

        </div>
        <button class="custom-btn" @click="goBack">BACK</button>
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
    goBack() {
      this.$router.go(-1)
    }
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

.movie-detail-infomation {
  margin-top: 5%;
  margin-right: 10%;
  text-align: left;
}

.moviedetail-title {
  font-weight: bold;
}

.star {
  position: relative;
  font-size: 32px;
  color: #ddd;
}

.star input {
  width: 100%;
  height: 100%;
  position: absolute;
  left: 0;
  opacity: 0;
}

.star span {
  width: 0;
  position: absolute;
  left: 0;
  color: red;
  overflow: hidden;
  pointer-events: none;
}

.genres-container {
  display: flex;
  flex-wrap: wrap;
}

.genre {
  margin-right: 10px;
}

</style>
