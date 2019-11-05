<template>
  <div class="signForm" :class="{'lds-box' : loadSpinner}">
    <div v-show="loadSpinner" class="lds-signup">
      <div class="lds-spinner"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    </div>
    <form autocomplete="off">
        <label for="username">username</label>
        <input type="text" id="username"  autocomplete="off" v-model="username">

        <label for="password">password</label>
        <input type="password" id="password" v-model="password">
        <span class="btn btn--primary" @click="registSend" style="margin-bottom: var(--space-sm); font-size: 20px; font-weight:500;">로그인</span>
        <div class="separater"></div>
        <span style="text-align: center; font-weight:700;"> Or</span>
        <span class="btn btn--google" style="margin-bottom: var(--space-sm);">
          <img :src="google_logo" alt="google_logo" style="width: 60px;margin-right:24px;" >
          Sign In with Google
        </span>
        <span class="btn btn--kakao">
          <img :src="kakao_logo" alt="google_logo" style="width: 50px; margin-right:26px; margin-left:6px;">
          Sign In with Kakao
        </span>
        <div class="separater"></div>
        <span style="text-align: center; font-weight:700;"> 아직 회원이 아니신가요?</span>
        <span class="btn btn--primary" @click="toggle_Sign" style="font-size: 20px; font-weight:500;">회원가입</span>



    </form>

  </div>
</template>

<script>
import api from '@/api'

export default {
  data() {
    return {
      username: '',
      password: '',
      loadSpinner: false,
      google_logo : require('@/assets/google_light.svg'),
      kakao_logo : require('@/assets/kakaotalk.svg')
    }
  },
  methods: {
    toggle_Sign() {
      this.$emit("toggle_Sign")
    },
    async registSend() {
      this.loadSpinner = true
      var res = await api.regist(this.username, this.password)

      setTimeout(() => {
        this.loadSpinner = false
        this.$router.push({ name: 'Introduce' })
      }, 3000);

    }
  }

}
</script>

<style>

</style>
