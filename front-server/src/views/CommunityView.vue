<template>
  <div class="mt-0">
    <div class="row">
      <ArticleList :articles="articleList" />
    <CreateArticleModal />
    </div>
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
    closeModal() {
      this.$store.commit('CLOSE_MODAL')
      this.getArticles()
    },
  },
}
</script>


<style>
/* .custom-btn {
  border: #000 solid 3px;
  border-radius: 0;
  background-color: transparent;
  margin: 0.5% 0.5% 0.5% 0.5%;
  float: right;
}

.custom-btn:hover {
  background-color: #000;
  color: #fff;
} */
</style>