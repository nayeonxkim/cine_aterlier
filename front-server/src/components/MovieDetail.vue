<template>
  <div>
    <h1>Movie Detail, {{movieId}}</h1>
  </div>
</template>

<script>
export default {
  // Django로 axios 요청 보내기
  data(){
    return {
      movieId : this.$route.params.movieId
    }
  },
  methods:{
    get_movie_item(movieId){
      this.$store.dispatch('get_movie_item', movieId)
    }
  },
  computed:{
    movieItem(){
      return this.$store.state.movieItem
    }
  },
  created(){
    this.get_movie_item()
  }
}
</script>

<style>

</style>