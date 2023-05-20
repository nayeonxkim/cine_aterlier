<template>
  <div class="first">
    <nav aria-label="Page navigation example">
      <ul class="pagination justify-content-center">
        <li class="page-item" @click="goToFirstPage">
          <a class="page-link" aria-label="First">
            <span class="first" aria-hidden="true" style="color: #000000">&laquo;</span>
          </a>
        </li>

        <li class="page-item" @click="onPrevious">
          <a class="page-link" aria-label="Previous">
            <span class="left" aria-hidden="true" style="color: #000000">&lsaquo;</span>
          </a>
        </li>

        <li class="page-item" v-for="(pageNum, id) in pageRange" :key="id" :class="{ active: pageNum === currentPage }" @click="onPageNum">
          <a class="page-link" style="color: #000000">{{ pageNum }}</a>
        </li>

        <li class="page-item" @click="onNext">
          <a class="page-link" aria-label="Next">
            <span class="right" aria-hidden="true" style="color: black;">&rsaquo;</span>
          </a>
        </li>

        <li class="page-item" @click="goToLastPage">
          <a class="page-link" aria-label="Last">
        <span class="last" aria-hidden="true" style="color: #000000">&raquo;</span>
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
    goToFirstPage() {
      if (this.currentPage === 1) {
        alert('첫 페이지입니다.')
      } else {
        this.currentPage = 1
        this.$store.dispatch('get_movie_list', this.currentPage)
        this.currentIndex = 1
        this.onPageNum({ target: { innerText: this.currentPage.toString() } })
      }
    },
    goToLastPage() {
      if (this.currentPage === 100) {
        alert('마지막 페이지 입니다.')
      } else {
        const lastPage = 100
        this.currentPage = lastPage
        this.$store.dispatch('get_movie_list', this.currentPage)
        this.currentIndex = parseInt((lastPage - 1) / 10) * 10 + 1
        this.onPageNum({ target: { innerText: this.currentPage.toString() } })
      }
    },
    onNext(){
      if (this.currentIndex < 91) {
        this.currentIndex = parseInt(this.currentIndex/10) * 10 + 11
        this.currentPage = this.currentIndex
        this.onPageNum({ target: { innerText: this.currentPage.toString() } })
      }
      else {
        alert('다음 페이지 목록이 없습니다.')
      }
    },
    onPrevious() {
      if (this.currentIndex > 10) {
        this.currentIndex = parseInt(this.currentIndex/10) * 10 - 1
        this.currentPage = this.currentIndex + 1
        this.onPageNum({ target: { innerText: this.currentPage.toString() } })
      } else {
        alert('이전 페이지 목록이 없습니다.')
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
.page-link {
  color: #000000;
  border-color: #fff !important;
}

.page-item.active .page-link, .page-item:focus, .left:active, .left:focus, .right:active, .right:focus, .first:active, .last:active {
  z-index: 1;
  color: #ff4429 !important;
  font-weight:bold;
  background-color: #fff !important;
  border-color: #fff;
}

.page-link:focus, .page-link:hover, .page-link:active, .left:hover, .left:focus, .right:hover, .right:focus, .first:hover, .first:focus, .last:focus, .last:hover {
  color: #ff4429 !important;
  background-color: #fff !important; 
  border-color: #fff !important;
  box-shadow: none !important;
}

</style>