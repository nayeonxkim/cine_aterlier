<template>
  <div class="Movie">
    <MovieList/>

  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'MovieView',
  components: {
    MovieList,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 페이지입니다.')
        this.$router.push({ name: 'login' })
      }
    }
  }
}
</script>

<style>

</style>