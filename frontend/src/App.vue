<template>
  <div id="app">
    <div>
      <nav>
        <div class="nav-items">
          <router-link :to="{ name: 'Home' }">SEMO</router-link>
          <router-link :to="{ name: 'Introduce' }">사이트소개</router-link>
          <router-link :to="{ name: 'Category' }">API 카테고리</router-link>
          <router-link :to="{ name: 'Journal' }">개발 일지</router-link>
        </div>
        <div class="nav-body">
          <input type="text">
          <fa-icon icon="user-alt"></fa-icon>
        </div>

      </nav>
      <router-view/>
      <footer>
        <div>
          <p>Install</p>
          <div>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took  a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries,  but also the leap into electronic typesetting,  remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing  Lorem Ipsum passages, and more recently  with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</div>
        </div>

        <div>
          <p>Giude</p>
          <div>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took  a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries,  but also the leap into electronic typesetting,  remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing  Lorem Ipsum passages, and more recently  with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</div>
        </div>

        <div>
          <p>Category</p>
          <div>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took  a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries,  but also the leap into electronic typesetting,  remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing  Lorem Ipsum passages, and more recently  with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</div>
        </div>
      </footer>
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

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Noto+Sans+KR:400,500,700,900|Noto+Sans:400,700,700i&display=swap&subset=korean');
  #app {
    font-family: 'Noto Sans', 'Noto Sans KR','Avenir', Helvetica, Arial, sans-serif ;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    padding-top: var(--space-xxl);
  }
</style>
