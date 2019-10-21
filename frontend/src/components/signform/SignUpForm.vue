<template>
  <div class="signForm">
    <form autocomplete="off">
        <label for="username">username</label>
        <input type="text" id="username">

        <label for="password">password</label>
        <input type="password" id="password">

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
        <span class="btn btn--primary" @click="toggle_Sign"  style="font-size: 20px; font-weight:500;">돌아가기</span>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return{

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
