<template>
  <div class="signForm" :class="{'lds-box' : loadSpinner}">
    <div v-show="loadSpinner" class="lds-signup">
      <div class="lds-spinner"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    </div>
    <form autocomplete="off">
        <label for="username">username</label>
        <input v-model="username" type="text" id="username">

        <label for="password">password</label>
        <input v-model="password" type="password" id="password">

        <label for="passwordConfirm">passwordConfirm</label>
        <input type="password" id="passwordConfirm">
        <label for="occupation">occupation</label>
        <select name="occupation" id="occupation">
          <option value="1">개발자</option>
          <option value="2">개발자</option>
          <option value="3">개발자</option>
          <option value="4">개발자</option>
          <option value="5">개발자</option>
          <option value="6">개발자</option>
          <option value="7">개발자</option>
        </select>

        <label for="occupation">language</label>
        <select name="occupation" id="occupation">
          <option value="1">파이썬</option>
          <option value="2">파이썬</option>
          <option value="3">파이썬</option>
          <option value="4">파이썬</option>
          <option value="5">파이썬</option>
          <option value="6">파이썬</option>
          <option value="7">파이썬</option>
        </select>
        <span class="btn btn--success" @click="registSend"  style="font-size: 20px; font-weight:500;">가입</span>
        <span class="btn btn--primary" @click="toggle_Sign"  style="font-size: 20px; font-weight:500; margin-top:10px;" >돌아가기</span>
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
