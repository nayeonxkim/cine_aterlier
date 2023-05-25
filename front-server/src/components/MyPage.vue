<template>
  <div v-if="userMypage" class="row text-left" style="font-family: 'Noto Sans KR', sans-serif;">
    <div class="col-1"></div>
    <div class="col-10" style="height:50%;">
      <!-- 사용자 이름 -->
      <h2>안녕하세요, {{ userMypage.username }}님</h2>
      <hr>
      <h2>내가 작성한 글</h2>
      <div v-if="userMypage.article_set.length === 0">
        <p>작성한 글이 없습니다.</p>
      </div>
      <div v-else class="row">
        <div class="article-item col-6" v-for="article in userMypage.article_set" :key="article.id" @click="goToDetail(article)">
          <div>
            <img style="width :60%; height:60%;" :src="`http://127.0.0.1:8000${article.img}`" alt="글 사진">
            <!-- <h2 class="article-title">제목: {{ article.title }}</h2> -->
          </div>
        </div>
      </div>
      <hr>
      <h2>내가 좋아요한 글</h2>
      <div v-if="userMypage.like_articles.length === 0">
        <p>좋아요한 글이 없습니다.</p>
      </div>
      <div v-else>
        <div class="article-row" v-for="likedArticle in userMypage.like_articles" :key="likedArticle.id" @click="goToDetail(likedArticle)">
          <div class="article-item">
            <img :src="`http://127.0.0.1:8000${likedArticle.img}`" alt="글 사진">
          </div>
        </div>
      </div>
      <hr>
      <div class="box">

      </div>
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
    goToDetail(article) {
      console.log(article.id)
      this.$router.push(`/articles/${article.id}`)
    },
  },
  created() {
    this.get_myPage()
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');
.text-left {
  text-align: left;
}

.box{
  height: 400px;
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
