<template>
  <div>
    <div class="test">
      <div class="main_header">
        <div>
          <p>당신을 위한 API 추천 사이트</p>
          <span>
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took  a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries,  but also the leap into electronic typesetting,  remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing  Lorem Ipsum passages, and more recently  with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
          </span>
        </div>
        <SignInForm/>
        <SignUpForm/>
      </div>
      <div>
        <p>Welcome home</p>
        <p>developers</p>
      </div>
    </div>
  </div>
</template>

<script>
import SignInForm from "@/components/signform/SignInForm"
import SignUpForm from "@/components/signform/SignUpForm"
export default {
  components: {
    SignInForm,
    SignUpForm
  }
}
</script>

<style lang="scss" scope>

</style>
