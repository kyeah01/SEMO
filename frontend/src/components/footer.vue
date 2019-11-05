<template>
  <footer>
        <ul>
          <li><span v-for="(item, index) in title" :key="index">| <div class="btn"> {{item}} </div> |</span></li>
          <li>Copyright ⓒ SEMO API. All rights Reserved.</li>
        </ul>
      </footer>
</template>

<script>
export default {
  name : "Footer",
  data() {
    return {
      title : ["회사소개", "이용약관", "개인정보처리방침", "고객센터"]
    }
  }
}
</script>

<style>

</style>
