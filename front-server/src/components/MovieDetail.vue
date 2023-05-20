<template>
  <div>
    <div class="modal fade"  tabindex="-1" :class="{ 'show': showModal }" > 
      <div class="modal-dialog modal-dialog-scrollable modal-xl">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="btn-close" @click="closeModal"></button>
          </div>
          <div class="modal-body">
            <!-- 모달 내용 -->
            <h5 class="modal-title">{{movieDetail.title}}</h5>
            <img :src="`https://image.tmdb.org/t/p/w500${movieDetail.poster_path}`" alt="">
            <p>{{movieDetail.release_date}}</p>
            <p v-for="genre in movieDetail.genres"
            :key="genre.id">{{genre.name}}</p>
            <p>{{movieDetail.runtime}}분</p>
            <p>{{movieDetail.popularity}}</p>
            <p>{{movieDetail.overview}}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="modal-backdrop" :class="{ 'show': showModal }"></div>
  </div>
</template>

<script>
export default {
  name:'MovieDetail',
  props: {
    movieId :Number 
  },
  data() {
    return {
      showModal: false
    };
  },
  computed:{
    movieDetail(){
      return this.$store.state.movieDetail
    }
  },
  methods:{
    closeModal() {
      this.showModal = false;
      this.$emit('close-modal');
    },
    get_movie_detail(){
      return this.$store.dispatch('get_movie_detail', this.movieId)
    }
  },

  mounted() {
    this.get_movie_detail()
    this.showModal = true; // 모달을 표시할 때 showModal 값을 true로 설정
  },
}
</script>

<style>
.modal {
  display: none;
  position: fixed;
  z-index: 1050;
  left: 0;
  top: 0;
  width: 100%;
  height: 10%;
  overflow: hidden;
  outline: 0;
}

.modal.show {
  display: block;
}

.modal-dialog {
  position: relative;
  width: 800px; 
  margin: 0%;
  pointer-events: none;
}

.modal-content {
  position: relative;
  display: flex;
  flex-direction: column;
  pointer-events: auto;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 0.3rem;
  outline: 0;
}

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  z-index: 1040;
  opacity: 0;
  transition: opacity 0.15s linear;
}

.modal-backdrop.show {
  opacity: 1;
}
</style>