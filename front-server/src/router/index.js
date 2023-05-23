import Vue from 'vue'
import VueRouter from 'vue-router'
// 영화정보
import MovieView from '../views/MovieView.vue'
import MovieList_Top100 from '../components/MovieList_Top100.vue'
import MovieDetail from '../components/MovieDetail.vue'


import HomeView from '../views/HomeView.vue'
import CommunityView from '../views/CommunityView.vue'

import LoginView from '../views/LoginView.vue'
import ArticleDetail from '../components/ArticleDetail.vue'
import ArticleUpdate from '../components/ArticleUpdate.vue'

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
        path: '/movie/Top100',
        name: 'movie-100',
        component: MovieList_Top100
      },
    ]
  },
  
  {
    path: '/movies/:movieId',
    name: 'movie-detail',
    component: MovieDetail
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView,
  },
  {
    path: '/articles/:articleId',
    name: 'article-detail',
    component: ArticleDetail,
  },
  {
    path:'/articles/:articleId/update',
    name:'article-update',
    component:ArticleUpdate
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
