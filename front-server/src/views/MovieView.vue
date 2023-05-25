<template>
  <div>
    <div class="genreBtn">

      <button v-for="(genre, idx) in genres" :key="idx" @click="filterMoviesByGenre(genre.id)" :class="{ active: isSelectedGenre(genre.id) }">
        {{ genre.name[0] }} | {{ genre.name[1] }}
      </button>
    </div>

    <div class="movie-row">
      <div v-for="(movie, idx) in nowShowMovie" :key="idx" class="movie-item">
        <MovieItem :movie-item="movie" />
      </div>
    </div>

    <div v-if="movieTop100" class="movie-row">
      <h1>인기영화 TOP 100</h1>
      <div v-for="(movie, idx) in movieTop100" :key="idx" class="movie-item">
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
          name:['액션', '어드벤처'],
        },
        {
          id:[16],
          name:['애니메이션', '어린이'],
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
      nowShowMovie: null, // 선택한 장르
      selectedGenre: null,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    movieTop100(){
      return this.$store.state.movieTop100
    }
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
    get_movie_100() {
      if (this.isLogin) {
        this.$store.dispatch('get_movie_100')
      } else {
        alert('로그인이 필요한 페이지입니다.')
        this.$router.push({ name: 'login' })
      }
    },

    filterMoviesByGenre(genreId) {
      this.$store.commit('IS_LOADING', true);
      this.$store.commit('GET_MOVIE_100_RESET');
      this.selectedGenre = genreId;
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

      setTimeout(() => {
      this.$store.commit('IS_LOADING', false); // 데이터 로딩 완료
    }, 2500);
    },

    isSelectedGenre(genreId) {
      return this.selectedGenre !== null && this.selectedGenre.toString() === genreId.toString();
    }
  },
  created(){
    this.get_movie_100()
    this.get_movie_List()
  },
}
</script>

<style>
.genreBtn {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.genreBtn > button {
  font-weight: 700;
  padding: 5px 10px;
  margin: 0 5px;
  border: #000 solid 3px;
  border-radius: 0;
  background-color: transparent;
}

.genreBtn > button.active {
  background-color: #000 !important;
  color: #fff !important;
}

.movie-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
}

.movie-row > .movie-item {
  flex-basis: 25%;
  padding: 10px;
  box-sizing: border-box;
}
</style>
