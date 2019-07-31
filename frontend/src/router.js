import Vue from 'vue'
import Router from 'vue-router'
import store from './store/store'

import Index from './views/Index.vue'
import Login from './views/Login.vue'

Vue.use(Router)

var router = new Router({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/index',
      name: 'index',
      component: Index,
      meta: {
        requireAuth: true,
        title: '首页'
      }
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import(/* webpackChunkName: "signup" */ './views/Signup.vue'),
      meta: {
        requireAuth: false,
        title: '注册'
      }
    },
    {
      path: '/',
      name: 'login',
      component: Login,
      meta: {
        requireAuth: false,
        title: '登录'
      }
    },
    {
      path: '/reset',
      name: 'reset',
      component: () => import(/* webpackChunkName: "reset" */ './views/Reset.vue'),
      meta: {
        requireAuth: false,
        title: '修改密码'
      }
    },
    {
      path: '/addevent',
      name: 'addevent',
      component: () => import(/* webpackChunkName: "addevent" */ './views/AddEvent.vue'),
      meta: {
        requireAuth: true,
        title: 'add event'
      }
    },
    {
      path: '/detail',
      name: 'detail',
      component: () => import(/* webpackChunkName: "detail" */ './views/Detail.vue'),
      meta: {
        requireAuth: true,
        title: 'detail'
      }
    }
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    // }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.meta.title) {
    document.title = to.meta.title
  }
  if (to.matched.some((r) => r.meta.requireAuth)) {
    if (store.state.is_login) {
      next()
    } else {
      next({
        path: '/'
      })
    }
  } else {
    next()
  }
})

export default router
