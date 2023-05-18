<template>
  <div>
    <h2>movie Item</h2>
    <img @click='goToDetail' :src="`https://image.tmdb.org/t/p/w500${movieItem.poster_path}`" :alt="`${movieItem.title}`">
  </div>
</template>

<script>
export default {
  name:'MovieItem',
  props:{
    movieItem : {},
  },
  methods:{

    goToDetail(){
      console.log()
      this.$router.push({name:'movie-detail', params:{movieId:this.movieItem.tmdb_id}})
    }
  }

}
</script>

<style>

</style>