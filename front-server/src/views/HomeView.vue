<template>
  <div class="home">
    <h1>이미지 생성</h1>
    
    <div id="karloImg" v-if="karloImgs">
      <KarloImgs 
   
      :karlo-imga="karloImgs"/>
      <!-- v-for="karloImg in karloImgs"
      :key="karloImg.id" -->

    </div>
      <!-- <div id="createdImg">생성된 이미지보여줄곳</div> -->
      <!-- <img src="/static/karloResults/5.png" alt=""> -->

    <div class="searchMovie">
      <h2>영화검색하기</h2>
    </div>
    <hr>

    <SearchModal />
  </div>
</template>

<script>
import SearchModal from '@/components/SearchModal.vue'
import KarloImgs from '@/components/KarloImgs.vue'
// @ is an alias to /src


export default {
  name: 'HomeView',
  components: {
    SearchModal,
    KarloImgs
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    movieId(){
      return this.$store.state.selectedMovie
    },
    karloImgs(){
      return this.$store.state.karloImgs
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if (!this.isLogin) {
        alert('로그인이 필요한 페이지입니다.')
        this.$router.push({ name: 'login' })
      }
    },
    // searchBar_reset(){
    //   return this.$store.commit('SEARCHBAR_RESET')
    // },
  },

  // destroyed(){
  //   this.searchBar_reset()
  // }

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