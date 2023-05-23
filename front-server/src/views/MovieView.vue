<template>
  <div>
    <!-- <h1>TOP 100 Popular</h1> -->
    <div class="genreBtn">

    <router-link to="/movie/Top100">인기 Top100</router-link>|
    <button v-for="genre in genres" :key="genre.id" @click="filterMoviesByGenre(genre.id)">
      {{ genre.name[0] }}/{{ genre.name[1] }}
    </button>
    </div>

    <router-view />

    <div v-for="movie in filteredMovies" :key="movie.id">
      {{movie}}
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieView',
  components: {
  },
  data(){
    return{
      genres:[
        {
          id:[35, 18],
          name:['코미디', '드라마'],
        },
        {
          id:[28, 12],
          name:['액션', '어드벤쳐'],
        },
        {
          id:[16],
          name:['애니메이션'],
        },
        {
          id:[80, 53],
          name:['범죄', '스릴러'],
        },
        {
          id:[27, 9648],
          name:['호러', '미스터리'],
        },
        {
          id:[878, 14],
          name:['SF', '판타지'],
        },
        {
          id:[10752, 36],
          name:['전쟁', '역사'],
        },
        {
          id:[10402, 99],
          name:['음악', '다큐멘터리'],
        },
      ],
      selectedGenre: null // 선택한 장르
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    filteredMovies() {
      if (this.selectedGenre) {
        return this.$store.state.movieList.filter(movie => movie.genre_id === this.selectedGenre);
      } else {
        return this.$store.state.movieListTop100;
      }
    }
  },
  methods: {
    get100List() {
      if (this.isLogin) {
        this.$store.dispatch('get100List')
      } else {
        alert('로그인이 필요한 페이지입니다.')
        this.$router.push({ name: 'login' })
      }
    }
  },
  created(){
    return this.get100List()
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