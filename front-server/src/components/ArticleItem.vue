<template>
  <div>
    <div class="card" @click="toDetail(articleItem)">
      <img :src="getFullImagePath(articleItem.img)" alt="Article Image" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">영화 제목</h5>
        <hr>
        <h6 class="card-subtitle mb-2 text-muted">화가 이름</h6>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    articleItem: Object
  },
  methods: {
    toDetail(article) {
      this.$emit('to-detail', article)
    },
    getFullImagePath(imageUrl) {
      const API_URL = 'http://127.0.0.1:8000'
      return `${API_URL}${imageUrl}`
    }
  }
}
</script>

<style scoped>
.card {
  width: 100%;
  height: 100%;
}
</style>
