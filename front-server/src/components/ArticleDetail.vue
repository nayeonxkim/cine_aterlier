<template>
  <div>
    <div v-if="article">
      <img
      :src="getFullImagePath(article.img)"
      style="width:50%; height:50%;"
      alt="Article Image">
      <h2>{{ article.title }}</h2>
      <p>{{ article.content }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import store from '@/store'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetail',
  data() {
    return {
      article: null,
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      const articleId = this.$route.params.articleId
      axios
        .get(`${API_URL}/articles/${articleId}`, {
          headers: {
            Authorization: `Token ${store.state.token}`
          }
        })
        .then(res => {
          this.article = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    getFullImagePath(imageUrl) {
      const API_URL = 'http://127.0.0.1:8000'
      return `${API_URL}${imageUrl}`
    }
  },
}
</script>

<style>

</style>
