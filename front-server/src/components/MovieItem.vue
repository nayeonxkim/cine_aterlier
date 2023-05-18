<template>
  <div>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <div class="col">
      <div class="card">
        <img :src="`https://image.tmdb.org/t/p/w500${movieItem.poster_path}`" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">{{movieItem.title}}</h5>
        </div>
      </div>
    </div>
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