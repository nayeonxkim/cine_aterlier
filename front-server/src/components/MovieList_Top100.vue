<template>
<div class="movie-list">
  <div class="row">
    <h1>Top100</h1>
      <MovieItem 
      v-for="(movie, idx) in movieList" 
      :key="idx"
      :movie-item= movie 
      class="col-3" />
  </div>


</div>
</template>

<script>
import MovieItem from "@/components/MovieItem.vue";

export default {
  name: 'MovieList_Top100',
  components: {
    MovieItem,
  },
  computed: {
    movieList() {
      return this.$store.state.movieList;
    },
     isLogin() {
      return this.$store.getters.isLogin
    }
  },
  // computed에서 getters isLogin받아옴!
  methods:{
    get100List() {
      if (this.isLogin) {
        this.$store.dispatch('get100List')
      } else {
        alert('로그인이 필요한 페이지입니다.')
        this.$router.push({ name: 'login' })
      }
    }
  },
  created(){
    return this.get100List()
  }
}
</script>

<style>
.movie-list {
  display: grid;
}
</style>