<template>
  <div>
    <h1>Article Detail</h1>
    <div v-if="article">
      <h2>{{ article.title }}</h2>
      <p>{{ article.content }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetail',
  data() {
    return {
      article: null, // 아티클 정보를 저장할 변수
    }
  },
  created() {
    this.getArticleDetail();
  },
  methods: {
    getArticleDetail() {
      const articleId = this.$route.params.articleId
      axios
        .get(`${API_URL}/articles/${articleId}/`)
        .then(response => {
          console.log(response.data)
          this.article = response.data
          console.log('성공!')
        })
        .catch(error => {
          console.log(error)
        });
    },
  },
}
</script>

<style>
/* 필요한 스타일을 추가하세요 */
</style>
