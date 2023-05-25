<template>
  <div class="article-list">
    <div class="row">
      <p>{{ userId }}</p>
      <div
        v-for="(article, idx) in articleList"
        :key="idx"
        class="col-6 col-md-4 col-lg-3 mb-4"
      >
        <ArticleItem :article-item="article" />
      </div>
    </div>
  </div>
</template>


<script>
import ArticleItem from '@/components/ArticleItem.vue'

export default {
  name: 'ArticleList',
  components: {
    ArticleItem,
  },
  computed: {
    articleList() {
      return this.$store.state.articleList
    },
    userId(){
      return this.$store.state.User.id
    }
  },
}
</script>

<style scoped>
.row {
  justify-content: space-between;
}

@media (max-width: 767px) {
  .col-md-4 {
    flex-basis: 50%;
  }
}

@media (min-width: 768px) and (max-width: 991px) {
  .col-lg-3 {
    flex-basis: 50%;
  }
}

.col-1, .col-3 {
  flex-basis: calc((100% - 2rem) / 12);
}

.col-1, .col-3 {
  flex-basis: calc((100% - 2rem) / 12);
}
</style>
