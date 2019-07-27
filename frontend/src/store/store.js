import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    is_login: false,
    user: undefined
  },
  mutations: {
    login (state, user) {
      state.is_login = true
      state.user = user
    },
    logout (state) {
      state.is_login = false
      state.user = undefined
    }
  }
})

export default store
