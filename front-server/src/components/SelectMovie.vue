<template>
  <div>
    <input @keyup.enter="get_searchedList" type="text" placeholder="영화제목을 입력하세요.">
    <button @click="get_searchedList" class="btn-btn-primary">검색</button>
    <SelectedMovie
    v-for="movie in searchedList"
    :key="movie.tmdb_id"
    :selected-movie="movie"
    />
  </div>
     
</template>

<script>
import SelectedMovie from '@/components/SelectedMovie.vue'
export default {
  name:'SelectMovie',
  components:{
    SelectedMovie
  },
  computed:{
    searchedList(){
      return this.$store.state.searchedList
    }
  },
  methods:{
    get_searchedList(event){
      this.$store.dispatch('get_searchedList', event.target.value)
      event.target.value = null
    },
    searchedList_reset(){
      this.$store.commit('SEARCHEDLIST_RESET')
    }
  },
  destroyed(){
    this.searchedList_reset()
  }
}
</script>

<style>

</style>