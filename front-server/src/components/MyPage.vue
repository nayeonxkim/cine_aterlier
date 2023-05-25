<template>
  <div class="text-left">
    <h1>마이페이지</h1>
    <h2>안녕하세요, {{ userMypage.username }}</h2>
    <hr>
    <h1>내가 작성한 글</h1>
    <h2 v-for="article in userMypage.article_set"
    :key="article.id"
    @click="goToDetail(article.id)">제목 : {{ article.title }}</h2>
    <hr>
    <h1>내가 좋아요한 글</h1>
    <h2 v-for="likedArticle in userMypage.like_articles"
    :key="likedArticle.id"
    @click="goToDetail(likedArticle.id)"
    >제목 : {{ likedArticle.title }}</h2>
    <hr>
    <p>{{ userMypage }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'MyPage',
  data(){
    return {
      userMypage : null
    }
  },
  methods:{
    get_myPage(){
      axios
      .get('http://127.0.0.1:8000/users/mypage/',{
        headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
      })
      .then((res)=>{
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
  created(){
    this.get_myPage()
  }
}
</script>

<style>

</style>