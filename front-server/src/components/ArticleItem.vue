<template>
  <div>
    <div class="card" @click="toDetail">
      <img :src="articleItem.img" class="card-img-top" alt="Article Image">
    </div>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    articleItem: Object
  },
  computed: {
    articleList() {
      return this.$store.state.articles
    }
  },
  methods: {
    toDetail() {
      const articleId = this.articleItem.id
      this.$router.push({ name: 'article-detail', params: { articleId: articleId } })
    }
  }
}
</script>