<template>
  <div class="signForm">
    <form autocomplete="off">
        <label for="username">username</label>
        <input type="text" id="username"  autocomplete="off">

        <label for="password">password</label>
        <input type="password" id="password">
        <span class="btn btn--primary" @click="toggle_Sign" style="margin-bottom: var(--space-sm); font-size: 20px; font-weight:500;">로그인</span>
        <div class="separater"></div>
        <span style="text-align: center;"> Or</span>
        <span class="btn btn--google" style="margin-bottom: var(--space-sm);">
          <img :src="google_logo" alt="google_logo" style="width: 60px;margin-right:24px;" >
          Sign In with Google
        </span>
        <span class="btn btn--kakao">
          <img :src="kakao_logo" alt="google_logo" style="width: 50px; margin-right:26px; margin-left:6px;">
          Sign In with Kakao
        </span>
        <div class="separater"></div>
        <span style="text-align: center;"> 아직 회원이 아니신가요?</span>
        <span class="btn btn--primary" @click="toggle_Sign" style="font-size: 20px; font-weight:500;">회원가입</span>



    </form>

  </div>
</template>

<script>
export default {
  data() {
    return{
      google_logo : require('@/assets/google_light.svg'),
      kakao_logo : require('@/assets/kakaotalk.svg')
    }
  },
  methods: {
    toggle_Sign() {
      this.$emit("toggle_Sign")
    }
  }

}
</script>

<style>

</style>
