<template>
  <div>
    <div>
      <h1>{{articleDetail.title}}</h1>
      <img
        :src="getFullImagePath(articleDetail.img)"
        style="width:20%; height:20%;"
        alt="Article Image"
      >
      <h5>{{ articleDetail.id }}번 게시글</h5>
      <p>{{ articleDetail.content }}</p>

      <button class="btn btn-primary" @click="$router.push(`/articles/${articleDetail.id}/update`)">UPDATE</button>
      <button class="btn btn-secondary" @click="deleteArticle">DELETE</button>
      <hr>

      <div class="comment-block">
        <input @keyup.enter="commentCreate" type="text" v-model="newComment.content" style="">
        <button class="btn btn-danger" @click="commentCreate">댓글 작성</button>
      </div>

      <ArticleComment 
      v-for="(comment, idx) in articleDetail.comment_set"
      :key="idx"
      :comment-item="comment"
      :article-id="articleDetail.id" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import store from '@/store'
import ArticleComment from '@/components/ArticleComment.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetail',
  computed: {
    articleDetail() {
      return this.$store.state.articleDetail
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
  components:{
    ArticleComment
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      const articleId = this.$route.params.articleId
      this.$store.dispatch('getArticleDetail', articleId)
    },
    getFullImagePath(imageUrl) {
      return `${API_URL}${imageUrl}`
    },
    deleteArticle() {
      axios
        .delete(`${API_URL}/articles/delete/${this.articleDetail.id}`, {
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
        .post(`${API_URL}/articles/${this.articleDetail.id}/comment_create/`,{ 
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

.comment-block{
  margin: 30px;
}

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
