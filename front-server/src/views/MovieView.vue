<template>
  <div>
    <h1>MovieView입니다</h1>

    <router-view />
    <PageNav />
  </div>
</template>

<script>
import PageNav from '@/components/PageNav.vue'

export default {
  name: 'MovieView',
  components: {
    PageNav
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