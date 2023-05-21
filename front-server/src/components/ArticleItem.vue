<template>
  <div>
    <div class="card" @click="toDetail(articleItem)">
      <img :src="getFullImagePath(articleItem.img)" alt="Article Image" class="card-img-top">
      <div class="card-body">
        <h6 class="card-title">영화 제목</h6>
        <hr>
        <h7 class="card-subtitle mb-2 text-muted">화가 이름</h7>
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

<style>

</style>
