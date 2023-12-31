import Vue from 'vue'
import VueRouter from 'vue-router'
// 영화정보
import MovieView from '../views/MovieView.vue'
import MovieList from '../components/MovieList.vue'


import HomeView from '../views/HomeView.vue'
import CommunityView from '../views/CommunityView.vue'

import LoginView from '../views/LoginView.vue'
import ArticleList from '../components/ArticleList.vue'
import ArticleDetail from '../components/ArticleDetail.vue'

Vue.use(VueRouter)


const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },

  // 영화정보
  {
    path: '/movie',
    name: 'movie',
    component: MovieView,
    children: [
      {
        path: '/movielist/:currentPage',
        name: 'movie-list',
        component: MovieList
      },
    ]
  },



  {
    path: '/community',
    name: 'community',
    component: CommunityView,
    children: [
      {
        path: '/articles/index',
        name: 'article-list',
        component: ArticleList,
      },
      {
        path: '/articles/:articleId',
        name: 'article-detail',
        component: ArticleDetail,
      },
    ]
  },
  {
    path: '/',
    name: 'login',
    component: LoginView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
