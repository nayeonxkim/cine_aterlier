<template>
  <div>
    <div class="card" @click="$router.push(`articles/${articleItem.id}`)">
      <img
      :src="getFullImagePath(articleItem.img)"
      class="card-img-top"
      style="width:100%; height:100%;"
      alt="Article Image">
      <div class="card-body">
        <h6 class="card-title">영화 제목</h6>
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
  computed: {
    articleList() {
      return this.$store.state.articleList
    }
  },
  methods: {
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
