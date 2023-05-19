import Vue from 'vue'
import VueRouter from 'vue-router'
// 영화정보
import MovieView from '../views/MovieView.vue'

import HomeView from '../views/HomeView.vue'
import CommunityView from '../views/CommunityView.vue'
import PersonalView from '../views/PersonalView.vue'
import PersonLogin from '../components/PersonLogin.vue'
import PersonSignup from '../components/PersonSignup.vue'
import ArticleList from '../components/ArticleList.vue'
import ArticleDetail from '../components/ArticleDetail.vue'

Vue.use(VueRouter)


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },

  // 영화정보
  {
    path: '/movie',
    name: 'movie',
    component: MovieView,

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
        component: ArticleDetail,
      },
    ]
  },
  {
    path: '/personal',
    name: 'personal',
    component: PersonalView,
    children: [
      {
        path: '/personlogin',
        name: 'personlogin',
        component: PersonLogin,
      },
      {
        path: '/personsignup',
        name: 'personsingup',
        component: PersonSignup,
      },
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
