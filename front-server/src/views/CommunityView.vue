<template>
  <div>
    <h1>Community</h1>
    <ArticlePageNav />
  </div>
</template>

<script>
import ArticlePageNav from '@/components/ArticlePageNav.vue'

export default {
  name: 'CommunityView',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  components: {
    ArticlePageNav,
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('get_article_list', 1)
      } else {
        alert('로그인이 필요한 페이지입니다.')
        this.$router.push({ name: 'login' })
      }
    },
  },
}
</script>

<style>

</style>