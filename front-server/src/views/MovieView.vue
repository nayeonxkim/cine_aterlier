<template>
  <div>
    <div class="genreBtn">
    <!-- <router-link to="/movie/Top100">인기 Top100</router-link>| -->
    <button v-for="(genre, idx) in genres" :key="idx" @click="filterMoviesByGenre(genre.id)">
      {{ genre.name[0] }}/{{ genre.name[1] }}
    </button>
    </div>
    <div class="movie-row">
      <div v-for="(movie, idx) in nowShowMovie" :key="idx" class="movie-item">
        <MovieItem :movie-item="movie" />
      </div>
    </div>
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem'
export default {
  name: 'MovieView',
  components: {
    MovieItem
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
      nowShowMovie: null // 선택한 장르
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  methods: {
    get_movie_List() {
      if (this.isLogin) {
        this.$store.dispatch('get_movie_List')
      } else {
        alert('로그인이 필요한 페이지입니다.')
        this.$router.push({ name: 'login' })
      }
    },
    get_movieTop100(){
      const movieTop100 = this.$store.state.movieList.slice(0,100);
      this.nowShowMovie = movieTop100
    },
    filterMoviesByGenre(genreId) {
      if (genreId.length === 2) {
        const genreId1 = genreId[0];
        const genreId2 = genreId[1];
        this.nowShowMovie = this.$store.state.movieList.filter(movie => {
          return movie.genre_id === genreId1 || movie.genre_id === genreId2;
        });
      } else {
        const genreId1 = genreId[0];
        this.nowShowMovie = this.$store.state.movieList.filter(movie => {
          return movie.genre_id === genreId1;
        });
      }
    }
  },
  created(){
    this.get_movie_List()
    this.get_movieTop100()
  },
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

.custom-btn {
  border: #000 solid 3px;
  border-radius: 0;
  background-color: transparent;
  margin: 0.5% 0.5% 0.5% 0.5%;
  /* padding: 2%;  여기 윈도우, 맥 호환 문제인지 확인 할 것 */
}

.custom-btn:hover {
  background-color: #000;
  color: #fff;
}

.movie-row {
  display: flex;
  flex-wrap: wrap;
}

.movie-row > div {
  width: 25%;
  padding: 10px;
  box-sizing: border-box;
}

</style>