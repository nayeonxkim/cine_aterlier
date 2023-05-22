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
      <button class="btn btn-primary" @click="openModal">UPDATE</button>
      <button class="btn btn-secondary" @click="deleteArticle">DELETE</button>
      <div class="mt-5">
        <div class="card mt-3" v-for="comment in article.community_set" :key="comment.id">
          <div class="card-body">
            <p class="card-text">{{ comment.content }}</p>
            <p class="card-subtitle text-muted">작성자: {{ comment.author }}</p>
          </div>
        </div>
      </div>
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
      showModal: false,
      newComment: {
        content: '',
        author: '',
      },
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
          this.getArticleComments() // 댓글 가져오기
        })
        .catch(err => {
          console.log(err)
        })
    },
    getArticleComments() {
      const articleId = this.$route.params.articleId;
      axios
        .get(`${API_URL}/articles/${articleId}`, {
          headers: {
            Authorization: `Token ${store.state.token}`,
          },
        })
        .then(res => {
          this.article.community_set = res.data.comment_set.map(comment => ({
            content: comment.content,
            author: comment.author,
          }));
        })
        .catch(err => {
          console.log(err);
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
        .then(() => {
          this.$router.push('/community')
        })
        .catch(err => {
          console.log(err)
        })
    },
    commentCreate() {
      const articleId = this.$route.params.articleId
      axios
        .post(`${API_URL}/articles/${articleId}/comment_create/`, this.newComment, {
          headers: {
            Authorization: `Token ${store.state.token}`,
          },
        })
        .then(() => {
          this.getArticleComments() // 댓글 업데이트
          this.newComment.content = ''
          this.newComment.author = ''
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
}
</script>

<style scoped>
.card {
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 10px;
}

.card-body {
  padding: 0;
}

.form-group {
  margin-bottom: 10px;
}
</style>
