<template>
  <div>
    <div v-if="article">
      <img
        :src="getFullImagePath(article.img)"
        style="width:50%; height:50%;"
        alt="Article Image"
      >
      <h2>{{ article.title }}</h2>
      <p>{{ article.content }}</p>
    </div>
    <button class="btn btn-primary" @click="openModal">UPDATE</button>
    <button class="btn btn-secondary" @click="deleteArticle">DELETE</button>
    <ArticleComments/>
  </div>
</template>

<script>
import axios from 'axios'
import store from '@/store'
import ArticleComments from './ArticleComments.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetail',
  components: {
    ArticleComments,
  },
  data() {
    return {
      article: null,
      showModal: false,
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
            Authorization: `Token ${store.state.token}`,
          },
        })
        .then(res => {
          this.article = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    getFullImagePath(imageUrl) {
      return `${API_URL}${imageUrl}`
    },
    openModal() {
      this.showModal = true
    },
    deleteArticle() {
      const articleId = this.$route.params.articleId
      axios
        .delete(`${API_URL}/articles/delete/${articleId}`, {
          headers: {
            Authorization: `Token ${store.state.token}`,
          },
        })
        .then(() => {  // 응답 결과 미사용
          this.$router.push('/community')
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
}
</script>

<style scoped>

</style>
