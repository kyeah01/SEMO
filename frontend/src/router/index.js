import Vue from 'vue'
import VueRouter from 'vue-router'

import MainPage from '@/views/MainPage'
import IntroducePage from '@/views/IntroducePage'
// categiry
import CategoryPage from '@/views/CategoryPage'
import APIDetail from '@/components/category/APIDetail'
import APIDetailT from '@/components/category/DetailT/APIDetailT'

import JournalPage from '@/views/JournalPage'
// admin
import AdminPage from '@/views/AdminPage'
import AdminMain from '@/components/admin/AdminMain'
import AdminPost from '@/components/admin/PostList'
import AdminReq from '@/components/admin/PostReq'

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
      { path: '/category/41', component: APIDetailT, name: 'APIDetailT' },
      { path: '/category/write', component: APIWrite, name: 'APIWrite' },
      { path: '/journal', component: JournalPage, name: 'Journal' },
      { path: '/profile', component: ProfilePage, name: 'ProfilePage' },
      {
        path: '/admin', component: AdminPage, name: 'Admin',
        children: [
          { path: 'main', component: AdminMain, name: 'Main'},
          { path: 'posts', component: AdminPost, name: 'API List'},
          { path: 'requests', component: AdminReq, name: 'API Req'},
        ]
      },
    ],
  })

  export default router
