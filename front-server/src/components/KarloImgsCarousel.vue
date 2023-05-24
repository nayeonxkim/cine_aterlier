<template>
  <div>
    <div v-if="karloImgs != null" id="finish">
      <h1>이미지가 완성되었어요 !</h1>
      <h3>영화 1: {{karloImgs[0].original_title1}}</h3>
      <h3>영화 2: {{karloImgs[0].original_title2}}</h3>
      <h3>선택한 화가: {{this.$store.state.selectedPainter}}</h3>
    </div>
    <div id="carouselExampleDark" class="carousel carousel-dark slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="http://127.0.0.1:8000/media/example.png" style="width: 30%; height: 30%;" alt="..1.">
        </div>
        <div class="carousel-item"
        v-for="karloImg in karloImgs"
        :key="karloImg.id">
           <img :src="`http://127.0.0.1:8000${karloImg.img_url}`" style="width: 30%; height: 30%;" alt="">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
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

  destroyed(){
    this.karloImgs_reset()
  }
}
</script>

<style>

</style>