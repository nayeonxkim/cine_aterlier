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
      <hr>
      <input type="text" v-model="newComment.content">
      <button class="btn btn-danger" @click="commentCreate">댓글 작성</button>
    <div v-for="(comment, idx) in article.comment_set"
    :key="idx"
    > {{comment.content}}</div>
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
        content: ''
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
          console.log(res.data)
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
      axios
        .delete(`${API_URL}/articles/delete/${this.article.id}`, {
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
      const userId = this.$store.state.User.id
      axios
        .post(`${API_URL}/articles/${this.article.id}/comment_create/`,{ content : this.newComment.content,
          author : userId },
        {
          headers: {
            Authorization: `Token ${store.state.token}`,
          },
        })
        .then((res) => {
          console.log(res)
          this.newComment.content = ''
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
