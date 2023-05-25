<template>
  <div class="row text-left">
    <div class="col-1"></div>
    <div class="col-10">
      <!-- 마이페이지 제목 -->
      <h1>마이페이지</h1>
      <!-- 사용자 이름 -->
      <h2>안녕하세요, {{ userMypage.username }}님</h2>
      <hr>
      <h1>내가 작성한 글</h1>
      <div v-if="userMypage.article_set.length === 0">
        <p>작성한 글이 없습니다.</p>
      </div>
      <div v-else>
        <div class="article-row" v-for="article in userMypage.article_set" :key="article.id" @click="goToDetail(article.id)">
          <div class="article-item">
            <img :src="`http://127.0.0.1:8000${article.img}`" alt="글 사진">
            <!-- <h2 class="article-title">제목: {{ article.title }}</h2> -->
          </div>
        </div>
      </div>
      <hr>
      <h1>내가 좋아요한 글</h1>
      <div v-if="userMypage.like_articles.length === 0">
        <p>좋아요한 글이 없습니다.</p>
      </div>
      <div v-else>
        <div class="article-row" v-for="likedArticle in userMypage.like_articles" :key="likedArticle.id" @click="goToDetail(likedArticle.id)">
          <div class="article-item">
            <img :src="likedArticle.image" alt="글 사진">
            <h2 class="article-title">제목: {{ likedArticle.img }}</h2>
            <h2 class="article-title">제목: {{ likedArticle.title }}</h2>
          </div>
        </div>
      </div>
      <hr>
      <p>{{ userMypage }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MyPage',
  data() {
    return {
      userMypage: null
    }
  },
  methods: {
    get_myPage() {
      axios
        .get('http://127.0.0.1:8000/users/mypage/', {
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
        .then((res) => {
          this.userMypage = res.data
        })
        .catch((err) => {
          console.error(err)
        })
    },
    goToDetail(articleId) {
      this.$router.push(`/articles/${articleId}`)
    },
  },
  created() {
    this.get_myPage()
  }
}
</script>

<style scoped>
.text-left {
  text-align: left;
}

.article-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
}

.article-row .article-item {
  cursor: pointer;
  margin-right: 20px;
  margin-bottom: 10px;
  text-align: center;
}

.article-row .article-item img {
  width: 200px;
  height: 200px;
  object-fit: cover;
}

.article-row .article-title {
  color: #007bff;
  font-weight: bold;
}

p {
  font-style: italic;
  color: #999;
}
</style>
