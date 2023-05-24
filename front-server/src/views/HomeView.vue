<template>
  <div class="home">
        
    <div v-if="isLoading">
      <h1>{{isLoading}}</h1>
      <h2>{{this.$store.state.isLoading}}</h2>
      <h2>로딩중이에요</h2>
      <hr>
    </div>
    
    <KarloImgsCarousel />
    <SearchModal 
    class="mt-5"/>
    <div class="box"></div>
  </div>
</template>

<script>
import SearchModal from '@/components/SearchModal.vue'
import KarloImgsCarousel from '@/components/KarloImgsCarousel.vue'
// @ is an alias to /src


export default {
  name: 'HomeView',
  components: {
    SearchModal,
    KarloImgsCarousel
  },
  computed: {
    isLoading(){
      return this.$store.state.isLoading
    },
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

.box{
  height: 500px;
  width: 500px;
}

.loading {
  z-index: 2;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: rgba(0, 0, 0, 0.1) 0 0 0 9999px;
}

.custom-btn {
  border: #000 solid 3px;
  border-radius: 0;
  background-color: transparent;
  margin: 0.5% 0.5% 0.5% 0.5%;
  padding: 2%;  /* 여기 윈도우, 맥 호환 문제인지 확인 할 것 */
}

.custom-btn:hover {
  background-color: #000;
  color: #fff;
}
</style>
