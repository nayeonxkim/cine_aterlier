<template>
  <div class="row">
    <div class="col-6" style="height: auto;">
      <img
        :src="getFullImagePath(articleDetail.img)"
        style="width: 100%; margin: 5%;"
        alt="Article Image"
      >
    </div>
    <div class="col-6 d-flex flex-column">
      <div class="text-right flex-grow-1" style="height: 100%;">
        <div class="temp" style="text-align: left; margin: 5%;">
          <h3 class="article-detail-title">{{ articleDetail.title }}</h3>
          <hr class="article-detail-horizen">
          <h5 class="article-detail-content">{{ articleDetail.content }}</h5>
        </div>
      </div>
      <div class="mt-0" style="text-right padding: 0px 0px">
        <button id="red-btn" class="custom-btn" style="padding: 5px 10px; margin-right: 3%" @click="deleteArticle">DELETE</button>
        <button class="custom-btn" style="padding: 5px 10px;" @click="$router.replace(`/articles/${articleDetail.id}/update`)">UPDATE</button>
      </div>
    </div>
    <hr>
    <div class="comment-block d-flex justify-content-between" style="margin: 0% 2.5%; padding: 0;">
      <div class="d-flex" style="width: 100%; padding: 0;">

        <input @keyup.enter="commentCreate" type="text"
        v-model="newComment.content" class="article-detail-input"
        style="margin-left: -1%; margin-right: 2%; padding: 0; height: 80%">

        <button class="custom-btn mt-0" style="padding: 5px 10px; margin-left: -0.8%; margin-right: 2%;;" @click="commentCreate">Add</button>
      </div>
    </div>
    <div class="col-12 comment-block">
      <ArticleComment
        v-for="(comment, idx) in articleDetail.comment_set"
        :key="idx"
        :comment-item="comment"
        :article-id="articleDetail.id"
        class="comment-item"
      />
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
.comment-item {
  margin-bottom: 10px;
}

.comment-content {
  flex: 1;
}

.custom-btn {
  font-weight: 700;
  padding: 5px 10px;
  border: #000 solid 3px;
  border-radius: 0;
  background-color: transparent;
}

.custom-btn:hover {
  background-color: #000 !important;
  color: #fff !important;
}

#red-btn:hover {
  background-color: #ff4429 !important;
  color: #000000 !important;
}

.page-btn {
  align-items: flex-end;
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

.article-detail-title {
  font-size: 300%;
}

.article-detail-content {
  margin-top: 10%;
  font-size: 150%;
  margin-bottom: auto;
  line-height: 3;
}

.article-detail-horizen {
  border-color: #000 !important;
}

.article-detail-input {
  border: 2px solid black;
  border-radius: 0;
  box-shadow: none;
  margin-top: 0.05%;
  height: 100%;
  width: calc(98% - 110px);
}

.custom-width {
  width: 80%;
}

.article-detail-input:focus,
.article-detail-input:active {
  border-color: black !important;
  box-shadow: none !important;
  border-radius: 0 !important;
}
</style>
