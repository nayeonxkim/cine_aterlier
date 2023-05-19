import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [
    ],
    token: null,
    // Movie
    movieList:null,
    movieItem:null,
    movieDetail:null

  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_ARTICLES_LIST(state, articles) {
      state.articles = articles
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      axios.defaults.headers.common['Authorization'] = `Token ${token}` // 헤더에 토큰 설정
    },
    LOGOUT(state) {
      state.token = null
      delete axios.defaults.headers.common['Authorization'] // 로그아웃 시 헤더에서 토큰 제거
    },
    // Movie의 mutations
    GET_MOVIE_LIST(state, payload){
      state.movieList = payload
    },
    GET_MOVIE_DETAIL(state,payload){
      state.movieDetail = payload
    }

  },
  actions: {
    // Login의 액션
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      
      axios({
        method: 'post',
        url:`${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
      .then((res) => {
        console.log(res)
        context.commit('SAVE_TOKEN', res.data.key)
        router.push({ name: 'home' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password
      
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password
        }
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        router.push({ name: 'home' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    logout(context) {
      return new Promise((resolve, reject) => {
        axios({
          method: 'post',
          url: `${API_URL}/accounts/logout/`,
          headers: {
            Authorization: `Token ${context.state.token}`
          }
        })
        .then(() => {
          context.commit('LOGOUT')
          resolve()
        })
        .catch((err) => {
          console.log(err)
          reject(err)
        })
      })
    },


    // Movie의 액션
    get_movie_list(context, currentPage){
      
      const start = 50 * (currentPage - 1)
      const end = (50 * currentPage)

      axios
      .get('http://127.0.0.1:8000/movies/index/')
      .then((res) => {
        const payload = res.data.slice(start,end)
        context.commit('GET_MOVIE_LIST', payload)
      })
      .catch((err) => {
        console.error(err)
      })
    },

    get_movie_detail(context, movieId){

      axios
      .get(`https://api.themoviedb.org/3/movie/${movieId}`,{
        params:{
          api_key:'42a52760a5d3f83a9c59c93e3265ddd7',
          language:'ko-KR'
      }})
      .then((res)=>{
        const payload = res.data
        context.commit('GET_MOVIE_DETAIL', payload)
      })
      .catch((err) => {
        
        console.error(err)
      })

    },

    // community의 액션
    get_article_list(context, currentPage) {
      // const start = 10 * (currentPage - 1)
      // const end = 10 * currentPage - 1
  
      axios
        .get(`${API_URL}/articles/index/`, {
          headers: {
            Authorization: `Token ${context.state.token}`
          }
        })
        .then((res) => {
          console.log(res)
          console.log(context)
          // const payload = res.data.slice(start, end)
          // console.log(payload)
          // context.commit('GET_ARTICLES_LIST', payload)
        })
        .catch((err) => {
          console.log(currentPage)
          console.log(err)
        })
    },
  },
  modules: {
  },
})
