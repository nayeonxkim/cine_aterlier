<template>
  <div style="font-family: 'Blinker', sans-serif;">
    <div v-if="karloImgs != null" id="finish" style="margin: 6% 0% 3%">
      <h3 style="margin-bottom: 1%;">{{ karloImgs[0].original_title1 }} & {{ karloImgs[0].original_title2 }}</h3>
      <h3>by {{ this.$store.state.selectedPainter }}</h3>
    </div>
    <div id="carouselExampleDark" class="carousel carousel-dark slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">

          <!-- 화면에 맞게 수정 필요 -->
          <img src="../assets/tip.png" style="width: 100%; height: 80%; margin: -10%">
          
        </div>
        <div class="carousel-item"
        v-for="karloImg in karloImgs"
        :key="karloImg.id">
           <img :src="`http://127.0.0.1:8000${karloImg.img_url}`" style="width: 35%; height: 35;" alt="">
        </div>
      </div>
      <button v-if="karloImgs != null" class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button v-if="karloImgs != null" class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name:'KarloImgsCarousel',
  computed:{
    karloImgs(){
      return this.$store.state.karloImgs
    },
  },
  methods:{
    karloImgs_reset(){
      return this.$store.commit('KARLOIMGS_RESET')
    }
  },

  // destroyed(){
  //   this.karloImgs_reset()
  // }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Blinker&family=Noto+Sans+KR:wght@700&display=swap');
</style>
