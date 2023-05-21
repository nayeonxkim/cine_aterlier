<template>
  <div>
    <div class="row">
      <ArticleList />
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
      return this.$store.state.articlesList;
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
      // 누른 페이지의 정보를 1자리에 넣어서 보내기
      this.$store.dispatch('get_article_list', 1)
    },
    closeModal() {
      this.$store.commit('CLOSE_MODAL')
    },
    toDetail(article) {
      const API_URL = 'http://127.0.0.1:8000'
      // ArticleDetail 페이지로 이동하는 메서드
      this.$router.push(`${API_URL}/articles/${article.id}`)
    }
  },
}
</script>

<style>
.row {
  margin-top: 10px;
}
</style>
