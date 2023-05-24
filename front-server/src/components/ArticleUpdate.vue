<template>
  <div class="row" style="margin-left: 4%;">
    <div class="col-4" style="height: auto;">
      <img
        :src="getFullImagePath(articleDetail.img)"
        style="width: 100%; margin: 5%;"
        alt="Article Image"
      >
    </div>
    <div class="col-7 d-flex flex-column" style="margin: 1% 3%;">
      <form @submit.prevent="submitForm" enctype="multipart/form-data">
        <div class="modal-body text-right flex-grow-1" style="height: 100%;">
          <div class="form-group">
            <label class="article-update" for="titleInput" style="display: block;">Title</label>
            <input
              id="titleInput"
              v-model="title"
              type="text"
              class="form-control"
              placeholder="Title"
              required
              style="margin-bottom: 5%"
            >
          </div>
          <div class="form-group" style="flex-grow: 1;">
            <label class="article-update" for="contentInput" style="display: block;">Content</label>
            <textarea
              id="contentInput"
              v-model="content"
              class="form-control"
              placeholder="Content"
              required
              style="margin-bottom: 5%; height: 100%;"
            ></textarea>
          </div>
        </div>
        <div class="modal-footer">
          <div style="display: flex; justify-content: space-between; margin-top: 10px;">
            <button type="submit" class="custom-btn" style="padding: 5px 10px;">SAVE</button>
            <button
              type="button"
              class="custom-btn"
              style="padding: 5px 10px;"
              @click="$router.push(`/articles/${articleDetail.id}`)"
            >
              BACK
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>



<script>
const API_URL = 'http://127.0.0.1:8000'
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
    getFullImagePath(imageUrl) {
      return `${API_URL}${imageUrl}`
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

<style scoped>
.article-update {
  /* font-weight: 700; */
  font-size: 150%;
  text-align: left;
}

#red-btn:hover {
  background-color: #ff4429 !important;
  color: #000000 !important;
}

.custom-btn {
  text-align: center;
  border: #000 solid 3px;
  border-radius: 0;
  padding: 0.5%;
  background-color: transparent;
}

.custom-btn:hover {
  background-color: #000;
  color: #fff;
}

.modal-footer{
  align-items: flex-end;
}
</style>