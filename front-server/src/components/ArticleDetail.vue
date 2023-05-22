<template>
  <div>
    <div v-if="article">
      <h5>{{ articleDetail.title }}번 게시글</h5>
      <p>{{ articleDetail.img }}</p>

      <img
        :src="getFullImagePath(article.img)"
        style="width:50%; height:50%;"
        alt="Article Image"
      >
      <!-- <h2>{{ articleTitle }}</h2> -->
      <!-- <p>{{ articleContent }}</p> -->
      <!-- <button class="btn btn-primary" @click="openModal">UPDATE</button>
      <button class="btn btn-secondary" @click="deleteArticle">DELETE</button>
      <hr> -->
      <!-- <input @keyup.enter="commentCreate" type="text" v-model="newComment.content"> -->
      <!-- <button class="btn btn-danger" @click="commentCreate">댓글 작성</button> -->
    <!-- <ArticleComment 
    v-for="(comment, idx) in article.comment_set"
    :key="idx"
    :comment-item="comment"
    :article-id="article.id" /> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import store from '@/store'
// import ArticleComment from '@/components/ArticleComment.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetail',
  computed: {
    articleDetail() {
      return this.$store.state.articleDetail;
    },
  },
  data() {
    return {
      article: null,
      showModal: false,
      newComment: {
        content: ''
      },
    }
  },
  // components:{
  //   ArticleComment
  // },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      const articleId = this.$route.params.articleId
      this.$store.dispatch('getArticleDetail', articleId)
        .then(response => {
          this.article = response.data
        })
        .catch(error => {
          console.log(error)
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
      axios
        .post(`${API_URL}/articles/${this.article.id}/comment_create/`,{ 
          content : this.newComment.content,
          },
        {
          headers: {
            Authorization: `Token ${store.state.token}`,
          },
        })
        .then(() => {
          this.newComment.content = ''
          this.getArticleDetail()
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
