<template>
  <div id="app">
    <div>
      <nav>
        <div>
          <router-link :to="{ name: 'Home' }">SEMO</router-link>
          <router-link :to="{ name: 'Home' }">사이트소개</router-link>
          <router-link :to="{ name: 'Home' }">API 커테고리</router-link>
          <router-link :to="{ name: 'Home' }">개발 일지</router-link>
        </div>
        <div>
          <input type="text">
        </div>
      </nav>
      <router-view/>
    </div>
  </div>
</template>

<script>
import router from "@/router";
import api from "./api";

export default {
  name: 'app',
  data() {
    return {
      name: '',
      pw: ''
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

<style>

</style>
