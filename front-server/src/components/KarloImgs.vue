<template>
  <div>
    <v-carousel>
    <v-carousel-item v-for="(item, index) in karloImgs" :key="index">
        <img :src="`http://127.0.0.1:8000${item.img_url}`" alt="Carousel Image">
      <!-- <img :src="`http://127.0.0.1:8000${karloImg.img_url}`" style="width: 200px; height: 200px;" alt=""> -->
    </v-carousel-item>
  </v-carousel>
  </div>
</template>

<script>
export default {
  name:'KarloImgs',
  props:{
    karloImgs:Object
  },
}
</script>

<style>

</style>