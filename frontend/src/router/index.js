import Vue from 'vue'
import VueRouter from 'vue-router'

import MainPage from '@/views/main'

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
      { path: '/main', component: MainPage, name: 'Home' },
    ],
  })
  
  export default router
  