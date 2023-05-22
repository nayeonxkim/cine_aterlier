<template>
  <div class="home">
    <KarloImgsCarousel />
    <SearchModal />
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
