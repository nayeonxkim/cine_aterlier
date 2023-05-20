<template>
  <div>
    <nav aria-label="Page navigation example">
      <ul class="pagination justify-content-center">
        <li class="page-item" @click="onPrevious">
          <a class="page-link" href="#" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>

        <li class="page-item" v-for="(pageNum, id) in pageRange" :key="id" :class="{ active: pageNum === currentPage }" @click="onPageNum">
          <a class="page-link" href="#">{{ pageNum }}</a>
        </li>

        <li class="page-item" @click="onNext">
          <a class="page-link" href="#" aria-label="Next">
            <span aria-hidden="true">&raquo;</span>
          </a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name:'PageNav',
  data(){
    return {
      currentPage : 1,
      currentIndex : 1,
    }
  },
  methods:{
    // li태그 클릭시
    // currentPage값을 li태그의 문자열로 바꿈.
    // get_movie_list액션을 실행하면서 currentPage 전달
    onPageNum(event) {
      const pageNum = event.target.innerText
      this.currentPage = parseInt(pageNum, 10)
      this.$store.dispatch('get_movie_list', this.currentPage)
    },
    onNext(){
      if (this.currentIndex < 91) {
        this.currentIndex = parseInt(this.currentIndex/10) * 10 + 11
        this.currentPage = this.currentIndex
      }
      else {
        alert('마지막 페이지입니다.')
      }
    },
    onPrevious() {
      if (this.currentIndex > 10) {
        this.currentIndex = parseInt(this.currentIndex/10) * 10 - 1
        this.currentPage = this.currentIndex + 1
      } else {
        alert('첫 페이지입니다.')
      }
    }
  },

  computed:{
    pageRange(){
      const startIndex = parseInt(this.currentIndex/10) * 10 + 1
      const endIndex =  parseInt(this.currentIndex/10)  * 10 + 11
      
      return _.range(startIndex, endIndex)
    }
  },
  watch:{
    currentPage(){
      this.$store.dispatch('get_movie_list', this.currentPage)
    }
  }
}
</script>

<style>
.page-item.active .page-link {
  background-color: #007bff;
  border-color: #007bff;
  color: #fff;
}

.page-item.active {
  background-color: #007bff;
}
</style>