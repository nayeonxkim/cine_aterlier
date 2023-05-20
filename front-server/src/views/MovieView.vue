<template>
  <div>
    <h1>ALL MOVIES</h1>
    <MovieList />
    <PageNav />
  </div>
</template>

<script>
import MovieList from '../components/MovieList.vue'
import PageNav from '@/components/PageNav.vue'

export default {
  name: 'MovieView',
  components: {
    MovieList,
    PageNav
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      if (this.isLogin) {
        this.$store.dispatch('get_movie_list', 1)
      } else {
        alert('로그인이 필요한 페이지입니다.')
        this.$router.push({ name: 'login' })
      }
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Blinker:wght@600&display=swap');
body{
  background-color: #fff4f4 !important;
}
h1{
  font-family: 'Blinker', sans-serif;
  margin: 30px !important;
}
</style>