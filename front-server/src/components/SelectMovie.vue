<template>
  <div class="justify-content-center align-items-center">
    <div class="row d-flex">
      <div class="col-md-1"></div>
      <div class="col-md-8">
        <input id="search-input" v-model="inputValue" @keyup.enter="get_searchedList" type="text" placeholder="영화 제목을 입력하세요.">
      </div>
      <div class="col-md-2">
        <button id="search-btn" @click="get_searchedList" class="custom-btn">SEARCH</button>
      </div>
      <div class="col-md-1"></div>
    </div>
    
    <div class="row">
      <SelectedMovie
        v-for="movie in searchedList"
        :key="movie.tmdb_id"
        :selected-movie="movie"
        id="selMovie"
        class="col-6 text-center"
        @click="selectMovie(movie)"
      />
    </div>
  </div>
</template>

<script>
import SelectedMovie from '@/components/SelectedMovie.vue'

export default {
  name: 'SelectMovie',
  components: {
    SelectedMovie
  },
  data() {
    return {
      inputValue: null
    }
  },
  computed: {
    searchedList() {
      return this.$store.state.searchedList
    }
  },
  methods: {
    get_searchedList() {
      if (!this.inputValue) {
        alert('영화 제목을 입력해주세요!')
        return
      }

      this.$store.dispatch('get_searchedList', this.inputValue)
      this.inputValue = null
    },
    selectMovie(movie) {
      // 선택한 영화의 selected 속성을 토글합니다.
      movie.selected = !movie.selected;
    }
  },
  watch: {
    searchedList(newValue) {
      if (newValue.length === 0) {
        alert('일치하는 영화를 찾을 수 없습니다.')
        this.$store.commit('SEARCHEDLIST_RESET')
      }
    }
  },
  destroyed() {
    this.$store.commit('SEARCHEDLIST_RESET')
  }
}
</script>

<style>

#search-input {
  margin-right: 20px;
  border: solid 3px black;
  padding-left: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
}

/* #search-btn {
  color: #fff;
  border: solid 0.5px black;
  background-color: black;
  border-radius: 13%;
  padding-right: 10px;
  padding-left: 10px;
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 5%;
}  */

.row {
  margin-top: 50px;
}

</style>
