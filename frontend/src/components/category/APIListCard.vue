<template>
  <div class="listCard">
    <div class="listCard-img" @click="imgClick">
      <img :src="imgSrc" alt="api image">
    </div>
    <div class="listCard-body">
      <p>Tmap API</p>
      <p class="listCard-tags">대중교통 | 유료 | 길게 쓰려고 테스트중입니다.</p>
      <p class="listCard-body">body</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ApiListCard',
  props: {
    item: {
      type: Object,
      required: true
    }
  },
  data: () => {
    return {
      imgSrc: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDQeGgiVPG1ZZ0xHgykZRyExvzN6FCUmcWLios_141CcHqdxPe'
    }
  },
  methods: {
    imgClick() {
      console.log('image click')
    }
  }
}
</script>

<style>
</style>
