<template>
  <div class="sidebar" :class="{'sidebar_expand' : chk_expand}">
    <div class="sidebar--main">
      <div class="sidebar--title">
        <h2>
          <slot name="title">title</slot>
        </h2>
      </div>
      <div class="sidebar--items">
        <ul>
          <slot name="list">items</slot>
        </ul>
      </div>
    </div>
    <div class="sidebar--expand_button-box"></div>
    <div class="sidebar--expand_button">
      <fa-icon icon="angle-right" @click="chk_expand = !chk_expand" id="exapnd_btn"></fa-icon>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SideBar',
  data() {
    return {
      chk_expand : true,
    }
  }
}
</script>

<style>

</style>
