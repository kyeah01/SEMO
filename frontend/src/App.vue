<template>
  <div id="app">
    <div>
      <router-link :to="{ name: 'Home' }">MainPage</router-link>
      <router-view/>
      <h2>로그인</h2>
      <form @submit.prevent="login">
        <p>
          <label for="loginID">id</label>
          <input v-model="name" type="text" id="loginID">
        </p>
        <p>
          <label for="loginPW">pw</label>
          <input v-model="pw" type="password" id="loginPW">
        </p>
        <button type="submit">submit</button>
      </form>
    </div>
    <div>
      input
      <div>
        <p>{{ name }}</p>
        <p>{{ pw }}</p>
      </div>
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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
