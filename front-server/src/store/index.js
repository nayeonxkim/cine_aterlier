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
    movieItem:null

  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'article-list' })
    },

    // Movie의 mutations
    GET_MOVIE_LIST(state, payload){
      state.movieList = payload
    },
    GET_MOVIE_ITEM(state, payload){
      state.movieItem = state.movieList.find(item => item.tmdb_id === payload)
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/articles/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then((res) => {
        // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },

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
          username, password
        }
      })
      .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err) => console.log(err))
    },

    // Movie의 액션
    get_movie_list(context){
      axios
      .get('http://127.0.0.1:8000/movies/index/')
      .then((res) => {
        const payload = res.data
        context.commit('GET_MOVIE_LIST', payload)
      })
      .catch((err) => {
        console.error(err)
      })
    },

    get_movie_item(context, movieId){
      const payload = movieId
      context.commit('GET_MOVIE_ITEM', payload)
    }
  },
  modules: {
  },
})
