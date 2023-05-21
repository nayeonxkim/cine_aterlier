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

        <li v-for="pageNum in pageRange" :key="pageNum" :class="{ 'page-item': true, active: pageNum === currentPage }">
          <a class="page-link" @click="onPageNum(pageNum)">{{ pageNum }}</a>
        </li>

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
import axios from 'axios'

export default {
  name: 'ArticlePageNav',
  data() {
    return {
      currentPage: 1,
      currentIndex: 1,
      articleCount: 0,
      articlesPerPage: 8,
    }
  },
  methods: {
    onPageNum(pageNum) {
      this.currentPage = pageNum
      this.$store.dispatch('get_article_list', this.currentPage)
    },
    onNext() {
      if (this.currentIndex < this.pageCountWithNavigation) {
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
    getArticleCount() {
      const API_URL = 'http://127.0.0.1:8000'
      const endpoint = `${API_URL}/articles/index/`

      axios
        .get(endpoint, {
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then((response) => {
          const articles = response.data.articles
          this.articleCount = articles.length
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  computed: {
    pageCount() {
      return Math.ceil(this.articleCount / this.articlesPerPage)
    },
    pageCountWithNavigation() {
      if (this.pageCount <= 10) {
        return this.pageCount
      } else {
        return Math.ceil(this.pageCount / 10) * 10
      }
    },
    pageRange() {
      const startIndex = (Math.ceil(this.currentIndex / 10) - 1) * 10 + 1
      const endIndex = Math.min(startIndex + 9, this.pageCount)

      return _.range(startIndex, endIndex + 1)
    },
  },
  watch: {
    currentPage(newValue) {
      if (newValue === 1) {
        this.currentIndex = 1
      } else if (newValue % 10 === 1) {
        this.currentIndex = newValue
      }
    },
    articleCount() {
      this.getArticleCount()
    },
  },
  mounted() {
    this.getArticleCount()
  },
}
</script>

<style>
.page-link {
  color: #000000 !important;
  border-color: #fff !important;
}

.page-item.active .page-link,
.page-item:focus,
.page-item:hover,
.left:active,
.left:focus,
.right:active,
.right:focus,
.first:active,
.last:active {
  z-index: 1;
  color: #ff4429 !important;
  font-weight: bold;
  background-color: #fff !important;
  border-color: #fff;
}

.page-link:focus,
.page-link:hover,
.page-link:active,
.left:hover,
.left:focus,
.right:hover,
.right:focus,
.first:hover,
.first:focus,
.last:focus,
.last:hover {
  color: #ff4429 !important;
  background-color: #fff !important;
  border-color: #fff !important;
  box-shadow: none !important;
}
</style>
