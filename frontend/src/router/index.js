import Vue from 'vue'
import VueRouter from 'vue-router'

import MainPage from '@/views/MainPage'
import IntroducePage from '@/views/IntroducePage'
// categiry
import CategoryPage from '@/views/CategoryPage'
import APIDetail from '@/components/category/APIDetail'

import JournalPage from '@/views/JournalPage'
// admin
import AdminPage from '@/views/AdminPage'
import AdminMain from '@/components/admin/AdminMain'
import AdminPost from '@/components/admin/PostList'

import APIWrite from '@/components/admin/post/APIWrite'

// Profile
import ProfilePage from '@/views/ProfilePage'

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
      { path: '/', component: MainPage, name: 'Home' },
      { path: '/semo', component: IntroducePage, name: 'Introduce' },
      { path: '/category', component: CategoryPage, name: 'Category' },
      { path: '/category/:apiId', component: APIDetail, name: 'APIDetail' },
      { path: '/category/write', component: APIWrite, name: 'APIWrite' },
      { path: '/journal', component: JournalPage, name: 'Journal' },
      { path: '/profile', component: ProfilePage, name: 'ProfilePage' },
      {
        path: '/admin', component: AdminPage, name: 'Admin',
        children: [
          { path: 'main', component: AdminMain, name: 'AdminMain'},
          { path: 'posts', component: AdminPost, name: 'AdminPost'},
        ]
      },
    ],
  })

  export default router
