<template>
  <div class="home">
    <MyMovieImage/>,
    <ChoiceList/>,
    <MyMovieList/>
  </div>
</template>

<script>
import MyMovieImage from '../components/MyMovieImage.vue'
import ChoiceList from '../components/ChoiceList.vue'
import MyMovieList from '../components/MyMovieList.vue'

// @ is an alias to /src


export default {
  name: 'HomeView',
  components: {
    MyMovieImage,
    ChoiceList,
    MyMovieList
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
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
        this.$router.push({ name: 'personlogin' })
      }
    }
  }
}
</script>
