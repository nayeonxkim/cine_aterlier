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
const API_URL = 'http://127.0.0.1:8000/'

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
      const articleId = this.$route.params.articleId;
      axios
        .get(`${API_URL}/articles/${articleId}/`) // Django API 엔드포인트 호출
        .then(response => {
          this.article = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
}
</script>

<style>

</style>
