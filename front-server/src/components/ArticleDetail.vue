<template>
  <div class="mt-0">
    <div class="mt-0">
      <div class="row">
        <div class="col-6">
          <img
            :src="getFullImagePath(articleDetail.img)"
            style="width: 100%; margin: 5%;"
            alt="Article Image"
          >
        </div>
        <div class="col-5 text-right">
          <div class="page-btn">
            <!-- 동일 링크 처리를 위한 replace 사용 -->
            <button class="custom-btn" @click="$router.replace(`/articles/${articleDetail.id}/update`)">UPDATE</button>
            <button id="red-btn" class="custom-btn" @click="deleteArticle">DELETE</button>
          </div>
          <div class="temp" style="text-align: left; margin-top: 15%;" >
            <h3>{{ articleDetail.title }}</h3>
            <!-- <h5>{{ articleDetail.id }}번 게시글</h5> -->
            <h5>{{ articleDetail.content }}</h5>
          </div>
        </div>
        <div class="col-6">
        </div>
      </div>
      <hr class="hori">
      <div class="comment-block">
        <input @keyup.enter="commentCreate" type="text" v-model="newComment.content" style="">
        <button class="custom-btn" @click="commentCreate">Add a Comment</button>
      </div>
    </div>
    <ArticleComment
      v-for="(comment, idx) in articleDetail.comment_set"
      :key="idx"
      :comment-item="comment"
      :article-id="articleDetail.id"
    />
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
.comment-block {
  margin: 30px;
}

.custom-btn {
  font-weight: 700;
  padding-right: 10px;
  padding-left: 10px;
  border: #000 solid 3px;
  border-radius: 0;
  background-color: transparent;
  float: right;
  margin-right: 10px;

}

.custom-btn:hover {
  background-color: #000 !important;
  color: #fff !important;
}

#red-btn:hover {
  background-color: #ff4429 !important;
  color: #000000 !important;
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
