<template>
  <div>
    <div class="row">
      <ArticleList :articles="articleList" />
    </div>
    <CreateArticleModal />
    <ArticlePageNav />
  </div>
</template>

<script>
import ArticleList from '../components/ArticleList.vue'
import ArticlePageNav from '@/components/ArticlePageNav.vue'
import CreateArticleModal from '../components/CreateArticleModal.vue'

export default {
  name: 'CommunityView',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    articleList() {
      return this.$store.state.articleList;
    },
  },
  components: {
    ArticleList,
    ArticlePageNav,
    CreateArticleModal,
  },
  created() {
    this.getArticleList()
  },
  methods: {
    getArticleList() {
      if (this.isLogin) {
        this.$store.dispatch('fetchArticleList', 1)
      } else {
        alert('로그인이 필요한 페이지입니다.')
        this.$router.push({ name: 'login' })
      }
    },
    closeModal() {
      this.$store.commit('CLOSE_MODAL')
    },
    toDetail(article) {
      const API_URL = 'http://127.0.0.1:8000'
      this.$router.push(`${API_URL}/articles/${article.id}`)
    }
  },
}
</script>
