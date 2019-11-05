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
      <div class="listDetail listDetail-guide">
        <APIDetailTop/>
      </div>
      <div class="listDetail listDetail-tall">
        <APIDetailMiddle/>
      </div>
      <div class="listDetail listDetail-guide">

        <APIDetailBottom/>
      </div>
    </div>
  </div>
  <div>

    <div class="btn btn-save btn-save-1 btn--success"
      @mouseover="save_hover = true"
      @mouseout="save_hover = false"
      @click="load_save"
      >
      <fa-icon v-if="!save_hover" :icon="['far', 'save']" style="z-index: 2;"></fa-icon>
      <fa-icon v-else icon="save" style="z-index: 2;"></fa-icon>
    </div>

    <div class="btn btn-save btn-save-2 btn--primary" @click="goList">
      <fa-icon icon="angle-left" style="z-index: 2;"></fa-icon>
    </div>
  </div>
  <div v-show="loadSpinner" class="lds-detail">
    <div class="lds-spinner"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
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
      loadSpinner: false,
      save_hover: false,
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
  mounted() {
    document.body.style.overflowX = 'hidden'
    document.body.style.overflowY = 'auto'
  },
  methods: {
    goList() {
      this.$router.go(-1)
      this.$emit('goList')
    },
    load_save() {
      this.loadSpinner = true
      setTimeout(() => {
        this.loadSpinner = false
      }, 1500)
    }
  }
}
</script>

<style lang="scss" scoped>
.btn {
  &-save {
    position: fixed;
    bottom: 50px;
    right: 75px;
    font-size: 50px;
    &-1 {
      right: 150px;
    }
    &-2 {
      width: 42px;
    }
  }
}
.lds-detail {
  z-index: 5;
  position: fixed;
  top: 50%;
  left: 50%;

}
</style>
