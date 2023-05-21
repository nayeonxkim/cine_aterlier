<template>
  <div>
    <div class="row">
      <ArticleItem
        v-for="(article, idx) in articleList"
        :key="idx"
        :article-item="article"
        class="col-6 col-md-3 col-lg-3 mb-4"
      />
    </div>
  </div>
</template>


<script>
import ArticleItem from './ArticleItem.vue'

export default {
  name: 'ArticleList',
  components: {
    ArticleItem,
  },
  computed: {
    articleList() {
      return this.$store.state.articleList
    },
  },
  beforeDestroy() {
    this.$store.commit('ARTICLELIST_RESET')
  },
};
</script>

<style>

</style>
