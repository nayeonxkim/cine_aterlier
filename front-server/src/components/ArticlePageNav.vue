<template>
  <div style="background-color: skyblue">
    <h2>ArticlePageNavbar</h2>

    <nav aria-label="Page navigation example">
      <ul class="pagination justify-content-center">
        <li class="page-item" @click="onPrevious">
          <a class="page-link" aria-label="Previous">
            <span aria-hidden="true" style="color: #000000">&laquo;</span>
          </a>
        </li>

        <template v-if="pageCount > 0">
          <li v-for="(pageNum, id) in pageRange" :key="id" :class="{ 'page-item': true, active: pageNum === currentPage }">
            <a class="page-link" @click="onPageNum(pageNum)">{{ pageNum }}</a>
          </li>
        </template>

        <template v-else>
          <li v-bind:class="{ 'page-item': true, active: currentPage === 1 }">
            <a class="page-link" @click="onPageNum(1)">1</a>
          </li>
        </template>

        <li class="page-item" @click="onNext">
          <a class="page-link" aria-label="Next">
            <span aria-hidden="true" style="color: #000000">&raquo;</span>
          </a>
        </li>
      </ul>
    </nav>
  </div>
</template>


<script>
import _ from 'lodash'
export default {
  name: 'ArticlePageNav',
  data() {
    return {
      currentPage: 1,
      currentIndex: 1,
      pageCount: 0,
    }
  },
  methods: {
    onPageNum(event) {
      const pageNum = event.currentTarget.innerText
      this.currentPage = parseInt(pageNum, 10)
      this.$store.dispatch('get_article_list', this.currentPage)
    },
    onNext() {
      if (this.currentIndex < this.pageCount) {
        this.currentIndex = parseInt(this.currentIndex / 10) * 10 + 11
        this.currentPage = this.currentIndex
      } else {
        alert('마지막 페이지입니다.')
      }
    },
    onPrevious() {
      if (this.currentIndex > 10) {
        this.currentIndex = parseInt(this.currentIndex / 10) * 10 - 1
        this.currentPage = this.currentIndex + 1
      } else {
        alert('첫 페이지입니다.')
      }
    },
  },

  computed: {
    pageRange() {
      const startIndex = parseInt(this.currentIndex / 10) * 10 + 1
      const endIndex = startIndex + 10

      const lastPage = Math.max(this.pageCount, 1) // 최소 페이지를 1로 설정

      return _.range(startIndex, Math.min(endIndex, lastPage + 1))
    },
  },

  watch: {
    '$store.state.articles'(newValue) {
      this.pageCount = Math.ceil(newValue.length / 10)
    },
  },
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
