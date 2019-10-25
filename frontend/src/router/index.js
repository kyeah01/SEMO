import Vue from 'vue'
import VueRouter from 'vue-router'

import MainPage from '@/views/MainPage'
import IntroducePage from '@/views/IntroducePage'
import CategoryPage from '@/views/CategoryPage'
import JournalPage from '@/views/JournalPage'
// admin
import AdminPage from '@/views/AdminPage'
import AdminPost from '@/components/admin/PostList'


Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
      { path: '/', component: MainPage, name: 'Home' },
      { path: '/semo', component: IntroducePage, name: 'Introduce' },
      { path: '/category', component: CategoryPage, name: 'Category' },
      { path: '/journal', component: JournalPage, name: 'Journal' },
      {
        path: '/admin', component: AdminPage, name: 'Admin',
        children: [
          { path: 'posts', component: AdminPost, name: 'AdminPost'},
        ]
      },
    ],
  })

  export default router
