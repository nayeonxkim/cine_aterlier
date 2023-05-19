<template>
  <div>
    <h1>{{movieId}}번 영화 디테일입니다</h1>
    <h2>{{movieDetail.title}}</h2>
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
    }
  },

  created(){
    this.get_movie_detail()
  },

  destroyed(){
    // this.$store.state.movieDetail를 null로 바꾸기.
  }
}
</script>

<style>

</style>