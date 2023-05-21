<template>
  <div>
    <div class="card" @click="toDetail(articleItem)">
      <h1>{{ articleItem.title }}</h1>
      <h2>{{ articleItem.content }}</h2>
      <img :src="getImagePath(articleItem.img)" alt="Article Image">
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
    getImagePath(imageUrl) {
      return this.$root.MEDIA_URL + imageUrl
    }
  }
}
</script>

<style>

</style>
