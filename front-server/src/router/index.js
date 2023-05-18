import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieDetail from '../components/MovieDetail.vue'
import HomeView from '../views/HomeView.vue'
import MovieView from '../views/MovieView.vue'
import CommunityView from '../views/CommunityView.vue'
import PersonalView from '../views/PersonalView.vue'
import PersonLogin from '../components/PersonLogin.vue'
import PersonSignup from '../components/PersonSignup.vue'

Vue.use(VueRouter)


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movie',
    name: 'movie',
    component: MovieView

  },
  {
    path: '/movie-detail/:movieId',
    name: 'movie-detail',
    component: MovieDetail

  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/personal',
    name: 'personal',
    component: PersonalView,
    children: [
      {
        path: '/personlogin',
        component: PersonLogin,
      },
      {
        path: '/personsignup',
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
