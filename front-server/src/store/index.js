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
    API_URL : 'http://127.0.0.1:8000',
    token: null,
    User: null,

    // Article
    articleList: null,
    selectedArticle: null,
    
    // Movie
    movieList:null,
    movieItem:null,
    movieDetail:null,

    // Home
    searchedList:null,
    selectedMovie:null

  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },

    // Article getters
    selectedArticle(state) {
      return state.selectedArticle
    },
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      axios.defaults.headers.common['Authorization'] = `Token ${token}` // 헤더에 토큰 설정
    },
    SET_USER(state, user) {
      state.User = user
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
    },


    // Article mutations
    GET_ARTICLE_LIST(state, article) {
      state.articleList = article
    },
    ARTICLELIST_RESET(state){
      state.articleList = null
    },
    SET_SELECTED_ARTICLE(state, article) {
      state.selectedArticle = article
    },

    // HOME의 mutations
    GET_SEARCHEDLIST(state, payload){
      state.searchedList = payload
    },
    SEARCHEDLIST_RESET(state){
      state.searchedList = null
    },
    SELECT_MOVIE(state, payload){
      state.selectedMovie = payload
    },
    SELECT_PAINTER(state, payload){
      state.selectedPainter = payload
    },
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
        context.commit('SET_USER', res.data)
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
        context.commit('SET_USER', res.data)
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
      const start = 8 * (currentPage - 1)
      const end = 8 * currentPage

      axios
        .get(`${API_URL}/articles/index/`, {
          headers: {
            Authorization: `Token ${context.state.token}`
          }
        })
        .then((res) => {
          const payload = res.data.slice(start, end)
          console.log(payload)
          context.commit('GET_ARTICLE_LIST', payload)
        })
        .catch((err) => {
          console.log(currentPage)
          console.log(err)
        })
    },
    
    get_article_detail(context, articleId){
      axios
      .get(`${API_URL}/articles/${articleId}`)
      .then((res)=>{
        const payload = res.data
        context.commit('GET_ARTICLE_DETAIL', payload)
      })
      .catch((err) => {
        console.error(err)
      })
    },
    create_article(context, formData) {
      formData.append('user', context.state.User)  // 사용자 정보 추가
      formData.append('userId', context.state.UserId)  // 사용자 ID 추가
  
      return new Promise((resolve, reject) => {
        axios
          .post(`${API_URL}/articles/create/`, formData, {
            headers: {
              Authorization: `Token ${context.state.token}`,
              'Content-Type': 'multipart/form-data',
            },
          })
          .then(() => {
            context.dispatch('get_article_list', 1)
            resolve()
          })
          .catch((error) => {
            reject(error)
          })
      })
    },
    setSelectedArticle({ commit }, article) {
      commit('SET_SELECTED_ARTICLE', article)
    },

    // HOME의 액션
    get_searchedList(context, movieTitle){
      axios
      .get(`http://127.0.0.1:8000/movies/index/`)
      .then((res) => {
        const searchedData = res.data.filter(obj => obj.title.includes(movieTitle));
        const payload = searchedData
        context.commit('GET_SEARCHEDLIST', payload)
      })
      .catch((err) => {
        console.error(err)
      })
    },

    to_karlo(context){
      console.log(context.state.selectedMovie)
      console.log(context.state.selectedPainter)
      axios
      .get(`http://127.0.0.1:8000/movies/karlo/${context.state.selectedMovie}/${context.state.selectedPainter}/`)
      .then((res) => {
        console.log(res)
        console.log(context)
      })
      .catch((err) => {
        console.error(err)
      })
  },
},
  modules: {
  },
})
