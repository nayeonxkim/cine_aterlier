<template>
  <div>
    <h1>{{movieDetail.title}}</h1>
    <img :src="`https://image.tmdb.org/t/p/w500${movieDetail.poster_path}`" alt="">
    <p>{{movieDetail.release_date}}</p>
    <p v-for="genre in movieDetail.genres"
    :key="genre.id">{{genre.name}}</p>
    <p>{{movieDetail.runtime}}분</p>
    <p>{{movieDetail.popularity}}</p>
    <p>{{movieDetail.overview}}</p>
  </div>
</template>

<script>
export default {
  name:'MovieDetail',
  data(){
    return{
      movieId : this.$route.params.movieId
    }
  },
  computed:{
    movieDetail(){
      return this.$store.state.movieDetail
    }
  },

  methods:{
    get_movie_detail(){
      return this.$store.dispatch('get_movie_detail', this.movieId)
    },
    movieDetail_reset(){
      return this.$store.commit('MOVIEDETAIL_RESET')
    }
  },

  created(){
    this.get_movie_detail()
  },

  destroyed(){
    this.movieDetail_reset()
    // this.$store.state.movieDetail를 null로 바꾸기.
  }
}
</script>

<style>

</style>