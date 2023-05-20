<template>
  <div>
    <div @click="openModal(movieItem.tmdb_id)">
      <!-- 포스터와 제목 보여주기 -->
      <img :src="`https://image.tmdb.org/t/p/w500${movieItem.poster_path}`" class="card-img-top" alt="Movie Poster">
      <p>{{movieItem.title}}</p>
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
.temp{
  width: 100%;
}
</style>