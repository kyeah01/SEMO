<template>
  <div class="sidebar" :class="{'sidebar_expand' : chk_expand}">

    <div class="sidebar--main">
      <div class="sidebar--title">
        <h2 v-if="PropData[0].title">{{PropData[0].title}}</h2>
      </div>

      <div class="sidebar--items">
        <ul v-for="item in PropData" :key="item.name">
          <li>{{item.name}}</li>
        </ul>
      </div>
    </div>

    <div class="sidebar--expand_button">
      <fa-icon icon="angle-right" @click="chk_expand = !chk_expand"></fa-icon>
    </div>

  </div>
</template>

<script>
export default {
  name: 'SideBar',
  props: {
    PropData: {
      type: Array,
      required: true
    },
  },
  data() {
    return {
      chk_expand : false,
    }
  }
}
</script>

<style>

</style>
