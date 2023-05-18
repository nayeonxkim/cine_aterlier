<template>
  <div>
    <h2>movie Item</h2>
    <p @click='goToDetail'>{{movieItem.title}}</p>
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