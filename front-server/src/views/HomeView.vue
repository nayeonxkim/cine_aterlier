<template>
  <div class="home">
    <h1>이미지 생성 영화 커뮤니티</h1>
    <div >
      <div id="createdImg">생성된 이미지보여줄곳</div>
      <img :src="getImageUrl(movieId)" alt="">
    </div>

    <div class="searchMovie">
      <h2>영화검색하기</h2>
    </div>
    <hr>
    <SearchModal />
  </div>
</template>

<script>
import SearchModal from '@/components/SearchModal.vue'
// @ is an alias to /src


export default {
  name: 'HomeView',
  components: {
    SearchModal
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    movieId(){
      return this.$store.state.selectedMovie
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 페이지입니다.')
        this.$router.push({ name: 'login' })
      }
    },
    searchBar_reset(){
      return this.$store.commit('SEARCHBAR_RESET')
    },
      getImageUrl(movieId) {
        return `http://127.0.0.1:8000/movies/getKarloImg/${movieId}/vangogh`;  // Django 서버의 도메인 주소로 대체해야 합니다.
    },
  },

  destroyed(){
    this.searchBar_reset()
  }

}
</script>

<style>

#createdImg{
  width: 500px;
  height: 500px;
  border: solid 1px black;
  background-color: brown;
}

</style>