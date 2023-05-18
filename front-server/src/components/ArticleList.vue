<template>
  <div>
    <h1>Article List</h1>
  </div>
</template>

<script>


export default {
  name: 'ArticleList',
  components: {
    // ArticleItem,
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
        this.$router.push({ name: 'personlogin' })
      }
    }
  }
}
</script>

<style>

</style>