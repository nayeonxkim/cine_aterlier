import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieList:null
  },
  getters: {
  },
  mutations: {
    GET_MOVIE_LIST(state, payload){
      state.movieList = payload
    }
  },
  actions: {
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
    }
  },
  modules: {
  }
})
