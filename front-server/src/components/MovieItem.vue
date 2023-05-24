<template>
  <div>
    <div @click="$router.push(`/movies/${movieItem.tmdb_id}`)" style="display: flex; justify-content: center;">
      <!-- 포스터와 제목 보여주기 -->
      <div class="movie-container">
        <div class="movie-image-container">
          <img :src="`https://image.tmdb.org/t/p/w500${movieItem.poster_path}`"
            alt="Avatar"
            class="image"
          >
          <div class="overlay">
            <h5><b>{{ movieItem.title }}</b></h5>
            <p>{{ movieItem.release_date }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>


export default {
  name: 'MovieItem',
  props:{
    movieItem:Object
  },
  data() {
    return {
      selectedMovieId: null,
    };
  },
  computed: {
    movieList() {
      return this.$store.state.movieList
    }
  },
  methods: {
  }
}
</script>


<style>
/* div {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
} */

* {
  box-sizing: border-box;
}

.movie-container {
  position: relative;
  width: 100%;
  max-width: 300px;
  height: auto;
  display: flex;
  justify-content: center;
  align-items: center;
}

.movie-image-container {
  position: relative;
  width: 100%;
  max-height: 0;
  padding-bottom: 140%;
  overflow: hidden;
}

.image {
  width: 100%;
  height: auto;
  object-fit: cover;
}

.overlay {
  position: absolute;
  bottom: 0;
  width: 100%;
  background: rgba(0, 0, 0, 0.8);
  color: #f1f1f1;
  transition: 0.5s ease;
  opacity: 0;
  color: white;
  font-size: 20px;
  padding: 20px;
  text-align: center;
  white-space: normal;
  overflow: hidden;
  text-overflow: ellipsis;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 35%;
}

.movie-container:hover .overlay {
  opacity: 1;
  white-space: normal;
  overflow: visible;
}
</style>