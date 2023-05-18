import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieDetail from '../components/MovieDetail.vue'
import HomeView from '../views/HomeView.vue'
import MovieView from '../views/MovieView.vue'

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
    path: '//movie-detail/:movieId',
    name: 'movie-detail',
    component: MovieDetail

  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
