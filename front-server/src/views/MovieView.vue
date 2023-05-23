<template>
  <div>
    <!-- <h1>TOP 100 Popular</h1> -->
    <div class="genreBtn">

    <router-link to="/movie/Top100">인기 Top100</router-link>
    <button>코미디/드라마 (35, 18)</button>
    <button>액션/어드벤쳐 (28, 12)</button>
    <button>애니메이션 (16)</button>
    <button>범죄/스릴러 (80, 53)</button>
    <button>호러/미스터리 (27, 9648)</button>
    <button>SF/판타지 (878, 14)</button>
    <button>전쟁/역사 (10752, 36)</button>
    <button>음악/다큐멘터리 (10402, 99)</button>
    </div>

    <router-view />
  </div>
</template>

<script>
export default {
  name: 'MovieView',
  components: {
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {

  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Blinker:wght@600&display=swap');

h1{
  font-family: 'Blinker', sans-serif;
  margin: 30px !important;
}

.genreBtn > button{
  border:solid 2px black;
}

</style>