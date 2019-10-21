<template>
  <div id="app">
    <div>
      <nav>
        <div class="nav-items">
          <router-link :to="{ name: 'Home' }" style="font-size:28px; font-weight:700;">SEMO</router-link>
          <router-link :to="{ name: 'Introduce' }">API란</router-link>
          <router-link :to="{ name: 'Category' }">API 카테고리</router-link>
          <router-link :to="{ name: 'Journal' }">개발 일지</router-link>

          <div class="nav-body">
            <input type="text" placeholder="Search" name="search" id="search">
            <label for="search" class="search-box"><fa-icon icon="search" class="nav-body_icon fa-search"></fa-icon></label>
          </div>
        </div>
        <div>
          <fa-icon icon="user-alt" class="nav-body_icon fa-user" @click="chk_profile = !chk_profile"></fa-icon>
          <fa-icon icon="power-off" class="nav-body_icon fa-off" @click="chk_profile = !chk_profile"></fa-icon>
        </div>
      </nav>




      <transition name="fade" mode="out-in">
        <router-view/>
      </transition>

    </div>
  </div>
</template>

<script>

import router from "@/router";
import api from "./api";

export default {
  name: 'app',
  components: {

  },
  data() {
    return {
      chk_search: false,
      chk_profile: false
    }
  },
  methods: {
    login() {
      this.name = ''
      this.pw = ''
      console.log('login')
    }
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Noto+Sans+KR:400,500,700,900|Noto+Sans:400,700,700i&display=swap&subset=korean');
  #app {
    user-select: none;
    font-family: 'Noto Sans', 'Noto Sans KR','Avenir', Helvetica, Arial, sans-serif ;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    padding-top: var(--space-xxxl);
  }
</style>
