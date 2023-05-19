<template>
  <div>
    <h1>Community</h1>
    <nav>
      <router-link to="/articlelist">Article List</router-link> |
      <router-link to="/articledetail">Article Detail</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
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