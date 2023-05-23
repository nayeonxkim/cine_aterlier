<template>
  <div>
      <h5 class="modal-title">{{movieDetail.title}}</h5>
      <img :src="`https://image.tmdb.org/t/p/w500${movieDetail.poster_path}`" alt="">
      <p>{{movieDetail.release_date}}</p>
      <p v-for="genre in movieDetail.genres"
      :key="genre.id">{{genre.name}}</p>
      <p>{{movieDetail.runtime}}분</p>
      <p>{{movieDetail.popularity}}</p>
      <p>{{movieDetail.overview}}</p>
       <div>
        <iframe :src="`https://www.youtube.com/embed/${movieTrailer[0].id.videoId}`" frameborder="0"></iframe>
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
        key : 'AIzaSyCDAEYnm8SkPW3utCcWiAtpmGPaEjEWG0Q',
        q : searchWord
      }})
      .then((response) =>{
        this.movieTrailer = response.data.items
      })
    },
  },

  created() {
    this.get_movie_detail()
    this.getTrailer()
  },
  mounted(){
    this.getTrailer()

  }
}
</script>

<style>
</style>