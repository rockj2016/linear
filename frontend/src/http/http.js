import axios from 'axios'
import qs from 'query-string'
import router from './../router'
import store from './../store/store'

class Http {
  constructor () {
    this.$http = axios.create({
      baseURL: 'http://94.191.56.131/',
      // baseURL: 'http://134.175.22.23:8899/',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      validateStatus: function (status) {
        return status < 500 // 状态码在大于或等于500时才会 reject
      },
      xsrfCookieName: 'csrftoken',
      xsrfHeaderName: 'X-CSRFToken'
    })
    this.dataMethodDefaults = {
      // headers: {
      //   'Content-Type': 'application/x-www-form-urlencoded',
      // //   'X-CSRFToken':get_token('csrftoken')
      // },
      transformRequest: [function (data) {
        return qs.stringify(data)
      }]
    }

    this.$http.interceptors.response.use(function (response) {
      if (response.status === 401) {
        console.log('未登陆')
        store.commit('logout')
        router.replace({ name: 'login', params: { go_check: false } })
      }
      // else if(response.status === 200){
      //     return response
      // }
      return response
      // else{
      //     let message =''
      //     if (response.data){
      //         message = response.data.info
      //     }
      //     alert(message)
      // return Promise.reject()
      // }
    }, function (error) {
      // 对响应错误做点什么
      console.log(error)
      return Promise.reject(error)
    })
  }

  signup (username, password, email) {
    let data = {
      username: username,
      password: password,
      email: email
    }
    return this.$http.post('signup/', data, { ...this.dataMethodDefaults })
  }

  login (username, password) {
    let data = {
      username: username,
      password: password
    }
    return this.$http.post('login/', data, { ...this.dataMethodDefaults })
  }

  logout () {
    return this.$http.get('logout/')
  }

  changePassword (data) {
    return this.$http.post('reset/', data, { ...this.dataMethodDefaults })
  }

  checkSession () {
    return this.$http.get('check_session/')
  }

  // 新建打卡
  addEvent (data) {
    return this.$http.post('event/', data, { ...this.dataMethodDefaults })
  }

  // 打卡列表
  eventList (data) {
    return this.$http.get('event/', data, { ...this.dataMethodDefaults })
  }

  // 记录
  addLog (data) {
    return this.$http.post('log/', data, { ...this.dataMethodDefaults })
  }
}

export default new Http()
