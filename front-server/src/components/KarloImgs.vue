<template>
  <div>
    <img :src="`http://127.0.0.1:8000${karloImg.img_url}`" style="width: 200px; height: 200px;" alt="">
    <!-- <p>{{karloImg.img_url}}</p> -->
  </div>
</template>

<script>
export default {
  name:'KarloImgs',
  props:{
    karloImg:Object
  },
  methods:{
    KarloImgs_reset(){
      return this.$store.commit('KARLOIMGS_RESET')
    }
  },
  destroyed(){
    this.KarloImgs_reset()
  }
}
</script>

<style>

</style>