import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState({
      paths: [
        'API_URL',
        'token',
        'User',
        'currentUser',
        // 'articleList',
        // 'articleDetail',
        // 'movieList',
        // 'movieItem',
        // 'movieDetail',
      //   'searchedList',
      //   'selectedPainter',
      //   'selectedMovie1',
      //   'selectedMovie2',
        'karloImgs',
      ]
    }),
  ],
  state: {
    API_URL : 'http://127.0.0.1:8000',
    token: null,
    User: null,
    currentUser : null,

    // Article
    articleList: null,
    articleDetail: null,

    // Movie
    movieList: null,
    movieItem: null,
    movieDetail: null,
    movieTop100:null,

    // Home
    searchedList: null,
    selectedPainter: 'null',
    selectedMovie1: null,
    selectedMovie2: null,
    karloImgs: null,
    axiosFail:false,

    // 로딩
    isLoading : false


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
      state.User = null
      delete axios.defaults.headers.common['Authorization'] // 로그아웃 시 헤더에서 토큰 제거
    },
    SET_CURRENT_USER(state, payload){
      state.currentUser = payload
    },

    // Movie의 mutations
    GET_MOVIE_LIST(state, payload){
      state.movieList = payload
    },
    GET_MOVIE_DETAIL(state, payload){
      state.movieDetail = payload
    },
    GET_MOVIE_100(state, payload){
      state.movieTop100 = payload
    },
    GET_MOVIE_100_RESET(state){
      state.movieTop100 = null
    },

    // Article mutations
    GET_ARTICLE_LIST(state, payload) {
      state.articleList = payload
    },
    GET_ARTICLE_DETAIL(state, payload) {
      state.articleDetail = payload
    },

    // HOME의 mutations
    GET_SEARCHEDLIST(state, payload){
      state.searchedList = payload
    },
    SEARCHEDLIST_RESET(state){
      state.searchedList = null
    },
    SELECT_MOVIE(state, payload){
      if(state.selectedMovie1 === null){
        state.selectedMovie1 = payload
      } else{
        state.selectedMovie2 = payload
      }
    },
    SELECT_PAINTER(state, payload){
      console.log(payload)
      state.selectedPainter = payload
    },
    TO_KARLO(state, payload){
      state.karloImgs = payload
    },
    KARLOIMGS_RESET(state){
      state.karloImgs = null
      state.selectedPainter = null
    },
    AXIOS_FAIL(state, payload){
      state.axiosFail = payload
    },
    SELECTEDMOVIE_RESET(state){
      state.selectedMovie1 = null
      state.selectedMovie2 = null
    },

    // 로딩
    IS_LOADING(state, payload){
      state.isLoading = payload
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
        // const userId = res.data.id; 
        console.log(res)
        context.commit('SAVE_TOKEN', res.data.key)
        context.commit('SET_USER', res.data)
        router.push({ name: 'home' })
      })
      .catch((err) => {
        console.error(err)
      })
    },

   
    getUserInfo(context){
 
      axios
      .get(`${API_URL}/users/info/`,
        {
          headers: {
            Authorization: `Token ${context.state.token}`,
          },
        })
        .then((res) => {
          const payload = res.data
          context.commit('SET_CURRENT_USER', payload)

        })
        .catch(err => {
          console.error(err)
        })
    },




    // fetchCurrentUser({ commit, getters, dispatch }) {

    //   // 토큰값 있으면 loggedin => true
    //   if (getters.isLoggedIn) {
    //     axios({
    //       url: drf.accounts.currentUserInfo(),
    //       method: 'get',
    //       // 토큰값 넣어서 정보 요청 합니다~ 
    //       headers: getters.authHeader,
    //     })
    //       // current user에 정보 저장
    //       .then(res => commit('SET_CURRENT_USER', res.data))
    //       // 실패하면 (토큰 오류임)
    //       .catch(err => {
    //         if (err.response.status === 401) {
    //           dispatch('removeToken')
    //           swal("다시 로그인해주세요!", {
    //             title: "오류",
    //             icon: "error",
    //             buttons: false,
    //             timer: 2000,
    //           })
    //           router.push({ name: 'start' })
    //         }
    //       })
    //   }
    // },







    
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
        this.dispatch('getUserInfo')
        context.commit('SAVE_TOKEN', res.data.key)
        context.commit('SET_USER', res.data)
        // router.push({ name: 'home' })
      })
      .catch((err) => {
        alert('username 혹은 password를 다시 확인해주세요.')
        console.error(err)
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
          console.error(err)
          reject(err)
        })
      })
    },

    // Movie의 액션
    get_movie_List(context) {
      context.commit('IS_LOADING', true); // 로딩 상태를 true로 변경
      
      axios
      .get('http://127.0.0.1:8000/movies/index/', {
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
      .then((res) => {
          const payload = res.data
          context.commit('GET_MOVIE_LIST', payload);
          context.commit('IS_LOADING', false); // 로딩 상태를 false로 변경 (응답 완료)
        })
        .catch((err) => {
          console.error(err);
          context.commit('IS_LOADING', false); // 로딩 상태를 false로 변경 (에러 발생)
        });
      },

      get_movie_100(context){
      context.commit('IS_LOADING', true); // 로딩 상태를 true로 변경
      
      axios
      .get('http://127.0.0.1:8000/movies/top100/', {
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
      .then((res) => {
          const payload = res.data
          context.commit('GET_MOVIE_100', payload);
          context.commit('IS_LOADING', false); // 로딩 상태를 false로 변경 (응답 완료)
        })
        .catch((err) => {
          console.error(err);
          context.commit('IS_LOADING', false); // 로딩 상태를 false로 변경 (에러 발생)
        });
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
      const start = 20 * (currentPage - 1)
      const end = 20 * currentPage
    
      axios
        .get(`${API_URL}/articles/index`, {
          headers: {
            Authorization: `Token ${context.state.token}`
          }
        })
        .then((res) => {
          const payload = res.data.articles.slice(start, end)
          context.commit('GET_ARTICLE_LIST', payload)
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
    getArticleDetail(context, articleId) {
      axios
        .get(`${API_URL}/articles/${articleId}/`, {
          headers: {
            Authorization: `Token ${context.state.token}`,
          },
        })
        .then((res) => {
          const payload = res.data
          context.commit('GET_ARTICLE_DETAIL', payload)
        })
        .catch((err) => {
          console.error(err)
        })
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
      context.commit('IS_LOADING', true)
      axios
      .get(`http://127.0.0.1:8000/movies/karlo/${context.state.selectedMovie1}/${context.state.selectedMovie2}/${context.state.selectedPainter}/`)
      .then((res) => {
        const payload = res.data
        context.commit('TO_KARLO', payload)
        context.commit('SELECTEDMOVIE_RESET')
        context.commit('IS_LOADING', false)
      })
      .catch((err) => {
        context.commit('IS_LOADING', false)
        context.commit('SELECTEDMOVIE_RESET')
        console.error(err)
        alert('부적절한 영화입니다!')
      })
  },
},
  modules: {
  },
})
