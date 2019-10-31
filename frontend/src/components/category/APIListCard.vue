<template>
  <div class="listCard">
    <div class="listCard-img" @click="apiSelect">
      <img :src="item.img" alt="api image" v-if="item.img">
      <img :src="imgSrc" alt="api image" v-else>
    </div>
    <div class="listCard-body">
      <p>{{ item.title }}</p>
      <p><span class="listCard-tags" v-for="(tag, index) in item.tags" :key="tag">{{ tag }} | </span></p>
      <p class="listCard-body">{{ item.body }}</p>
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
    },
  },
  data: () => {
    return {
      imgSrc: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDQeGgiVPG1ZZ0xHgykZRyExvzN6FCUmcWLios_141CcHqdxPe'
    }
  },
  methods: {
    apiSelect() {
      this.$emit('select', this.item)
    }
  }
}
</script>

<style>
</style>
