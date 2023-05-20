<template>
  <div>
    <div @click="openModal(movieItem.tmdb_id)">
      <!-- 포스터와 제목 보여주기 -->
      <img 
      :src="`https://image.tmdb.org/t/p/w500${movieItem.poster_path}`" 
      class="card-img-top" 
      style="width:330px; height:460px;"
      alt="Movie Poster">
      <p id="movie-title">{{movieItem.title}}</p>
      <hr id="movie-hr">
      <p>{{movieItem.release_date}}</p>
    </div>

     <MovieDetail
      :movie-id="selectedMovieId"
      v-if="showModal"
      @close-modal="closeModal"
      class="temp"
    />
  </div>
</template>

<script>
import MovieDetail from '@/components/MovieDetail.vue'
export default {
  name: 'MovieItem',
  props:{
    movieItem:Object
  },
  components:{
    MovieDetail
  },
  data() {
    return {
      selectedMovieId: null,
      showModal: false
    };
  },
  computed: {
    movieList() {
      return this.$store.state.movieList
    }
  },
  methods: {
    openModal(movieId) {
      this.selectedMovieId = movieId;
      this.showModal = true;
    },
    closeModal() {
      this.selectedMovieId = null;
      this.showModal = false;
    }
  }
}
</script>

<style>

@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');

img{
  margin-bottom: 2px;
}

#movie-title{
  font-size:25px !important;
}

div {
  font-family: 'Noto Sans KR', sans-serif;
}

.temp{
  width: 100%;
}

#movie-hr{
  
  height:3px; 
  border-color: #000000;
  margin-left : auto;
  margin-right : auto;
}
</style>