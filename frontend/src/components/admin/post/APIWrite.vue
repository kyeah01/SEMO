<template>
<div>
  <Sidebar>
    <template v-slot:title>
      <h2>{{ sideBarItems[0].title }}</h2>
    </template>
    <template v-slot:list>
      <li v-for="item in sideBarItems.slice(2, sideBarItems.length)" :key="item.name" @click="formFilter(item.id)">{{ item.name }}</li>
    </template>
  </Sidebar>

  <div class="apiDetail">
    <div class="listDetail-content">
      <div v-show="loadSpinner" class="lds-detail">
        <div class="lds-spinner"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
      </div>
      <div class="listDetail">
        <fa-icon icon="times" @click="goList" style="z-index: 2;"></fa-icon>
        <APIDetailTop/>
      </div>
      <div class="listDetail">
        <APIDetailMiddle/>
      </div>
      <div class="listDetail listDetail-guide">

        <APIDetailBottom/>
      </div>
    </div>
  </div>

</div>
</template>

<script>
import Sidebar from "@/components/sidebar"

import APIDetailTop from './APIDetailTop'
import APIDetailMiddle from './APIDetailMiddle'
import APIDetailBottom from './APIDetailBottom'

export default {
  components: {
    APIDetailTop,
    APIDetailMiddle,
    APIDetailBottom,
    Sidebar
  },
  data: () => {
    return {
      loadSpinner: true,
      sideBarItems : [
        {title : 'New API'},
        {subtitle : ''},
        {name: 'API Category', id:1},
        {name: 'API Introduce', id:2},
        {name: 'How to use', id:3},
        {name: 'Dev Guide', id:4},
        {name: 'Parameters', id:6},
        {name: 'Responses', id:7},
      ],
    }
  },
  watch: {
    loadSpinner() {
      if (this.loadSpinner) {
        document.body.style.overflowY = 'hidden'
      }
      document.body.style.overflowY = 'auto'
    }
  },
  mounted() {
    document.body.style.overflowX = 'hidden'
    document.body.style.overflowY = 'hidden'
    this.loadData()
  },
  methods: {
    goList() {
      this.$router.go(-1)
      this.$emit('goList')
    },
    loadData() {
      setTimeout(() => {
        this.loadSpinner = false
      }, 1000);
    }
  }
}
</script>

<style>

</style>
