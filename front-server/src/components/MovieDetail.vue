<template>
  <div>
    <div class="row">
      <div class="col-md-1"></div>
      <div class="col-md-10">
        <img :src="`https://image.tmdb.org/t/p/original${movieDetail.backdrop_path}`" alt="" width="80%" height="100%">
      </div>
      <div class="col-md-1"></div>
    </div>


    <div class="row pt-5 pb-5 pl-0">
      <div class="col-md-1"></div>
      <div class="col-md-3 pl-0">
        <img :src="`https://image.tmdb.org/t/p/original${movieDetail.poster_path}`" alt="">
      </div>
      <div class="col-md-6">
        <div class="movie-detail-infomation">
          <h5 class="moviedetail-title">{{ movieDetail.title }}   {{ movieDetail.original_title }}</h5>

         <div class="star-ratings">
            <div 
              class="star-ratings-fill"
              :style="{ width: ratingToPercent + '%' }"
            >
              <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
            </div>
            <div class="star-ratings-base">
              <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
            </div>
          </div>

          <div class="genres-container">
            <span v-for="genre in movieDetail.genres" :key="genre.id" class="genre">{{ genre.name }}</span>
            <p>{{ movieDetail.runtime }}분</p>
          </div>
          <p>{{ movieDetail.release_date }}</p>
          <p>{{ movieDetail.overview }}</p>
        </div>
        <button class="custom-btn" @click="goBack">BACK</button>
      </div>
      <div class="col-md-1"></div>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    movieId() {
      return this.$route.params.movieId;
    },
    movieDetail() {
      return this.$store.state.movieDetail;
    },
    ratingToPercent() {
      const score = +(this.movieDetail.vote_average/2) * 20;
      return score + 1.5;
    }
  },
  methods: {
    goBack() {
      this.$router.back();
    },
  },
  mounted() {
    this.$store.dispatch('get_movie_detail', this.movieId);
  }
}
</script>

<style>
.star-ratings {
  color: #aaa9a9; 
  position: relative;
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1.3px;
  -webkit-text-stroke-color: #2b2a29;
}
 
.star-ratings-fill {
  color: #fff58c;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: gold;
}


.star-ratings span {
  font-size: 32px; /* Adjust the size as needed */
}

.star-ratings-fill span {
  font-size: 32px; /* Adjust the size as needed */
}

.star-ratings-base {
  z-index: 0;
  padding: 0;
}

.movie-detail-infomation {
  margin-top: 5%;
  margin-right: 10%;
  text-align: left;
}

.moviedetail-title {
  font-weight: bold;
}

.genres-container {
  display: flex;
  flex-wrap: wrap;
}

.genre {
  margin-right: 10px;
}
</style>
