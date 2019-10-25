import Vue from 'vue'
import VueRouter from 'vue-router'

import MainPage from '@/views/MainPage'
import IntroducePage from '@/views/IntroducePage'
import CategoryPage from '@/views/CategoryPage'
import JournalPage from '@/views/JournalPage'

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
      { path: '/', component: MainPage, name: 'Home' },
      { path: '/semo', component: IntroducePage, name: 'Introduce' },
      { path: '/category', component: CategoryPage, name: 'Category' },
      { path: '/journal', component: JournalPage, name: 'Journal' },
    ],
  })

  export default router
