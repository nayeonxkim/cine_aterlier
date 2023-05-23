<template>
  <div>
    <h1>제목 : {{articleDetail.title}}</h1>

    <form @submit.prevent="submitForm" enctype="multipart/form-data">
      <div class="modal-body">
        <div class="form-group">
          <label for="titleInput">Title:</label>
          <input id="titleInput" v-model="title" type="text" class="form-control" placeholder="Title" required>
        </div>
        <div class="form-group">
          <label for="contentInput">Content:</label>
          <textarea id="contentInput" v-model="content" class="form-control" placeholder="Content" required></textarea>
        </div>
        </div>
        <div class="modal-footer">
          <button type="submit" class="btn btn-primary">수정</button>
          <button type="button" class="btn btn-secondary"
          @click="$router.push(`/articles/${articleDetail.id}`)">취소</button>
        </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return {
      title:'',
      content: ''
    }
  },
  computed:{
    articleId(){
      return this.$route.params.articleId
    },
    articleDetail() {
      return this.$store.state.articleDetail
    },
  },

  methods:{
    getArticleDetail() {
      this.$store.dispatch('getArticleDetail', this.articleId)
      this.title = this.articleDetail.title
      this.content = this.articleDetail.content
    },
    submitForm() {
      const API_URL = 'http://127.0.0.1:8000'
      const formData = new FormData()
      formData.append('title', this.title)
      formData.append('content', this.content)

      // 유저 정보 가져오기
      const user = this.$store.state.User
      if (user) {
        formData.append('author', user.id)
      }

      axios
      .put(`${API_URL}/articles/update/${this.articleId}/`, formData, {
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
          'Content-Type': 'multipart/form-data',
        },
      })
      .then(() => {
        console.log(this.Authorization)
        this.$store.dispatch('get_article_list', 1)
        this.title = ''
        this.content = ''
        this.$router.push(`/articles/${this.articleDetail.id}`)
      })
      .catch((error) => {
        console.error(error)
      })
    }
  },
  created(){
    this.getArticleDetail()
  }
  
}
</script>

<style>

</style>