<template>
  <div>
    <h1>Community</h1>
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
      this.$store.dispatch('get_article_list', 1)
    },
    closeModal() {
      this.$store.commit('CLOSE_MODAL')
    },
  },
}
</script>

<style>

</style>
