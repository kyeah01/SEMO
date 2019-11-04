<template>
  <div>
      <div class="main_header">
        <img class="main_header-img" src="https://uploads.actionvfx.com/header_photo/spina/article/222/6-Common-Nodes-for-Nuke-Beginners-Banner-compressor.jpg" alt="">
        <transition name="fade" mode="in-out">
          <SignInForm v-if="chk_Sign" @toggle_Sign="toggle_Sign"/>
          <SignUpForm v-if="!chk_Sign" @toggle_Sign="toggle_Sign"/>
        </transition>
      </div>
      <Footer/>
  </div>
</template>

<script>
import Footer from "@/components/footer"
import SignInForm from "@/components/signform/SignInForm"
import SignUpForm from "@/components/signform/SignUpForm"
export default {
  components: {
    Footer,
    SignInForm,
    SignUpForm
  },
  data() {
    return {
      chk_Sign : true,
    }
  },

  methods: {
    toggle_Sign() {
      this.chk_Sign = !this.chk_Sign
    }
  }
}
</script>

<style lang="scss" scope>

</style>
