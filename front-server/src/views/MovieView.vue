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
          name:['Comedy', 'Drama'],
        },
        {
          id:[28, 12],
          name:['Action', 'Adventure'],
        },
        {
          id:[16],
          name:['애니메이션', '어린이'],
        },
        {
          id:[80, 53],
          name:['Crime', 'Thriller'],
        },
        {
          id:[27, 9648],
          name:['Horror', 'Mistery'],
        },
        {
          id:[878, 14],
          name:['SF', 'Fantasy'],
        },
        {
          id:[10752, 36],
          name:['War', 'History'],
        },
        {
          id:[10402, 99],
          name:['Music', 'Documentary'],
        },
      ],
      nowShowMovie: null, // 선택한 장르
      selectedGenre: null // 선택된 장르 ID
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
    },
    isSelectedGenre(genreId) {
      return this.selectedGenre !== null && this.selectedGenre.toString() === genreId.toString();
    }
  },
  created(){
    this.get_movie_List()
    this.get_movieTop100()
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
