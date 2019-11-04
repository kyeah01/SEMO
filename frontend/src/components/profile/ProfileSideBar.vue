<template>
  <div class="profile_SideBar">
      <div class="profile_SideBar--img">
        <img :src="userImg" alt="userimg" style="max-width: 190px; max-height: 200px;">
      </div>
      <div class="profile_SideBar--title">
        SEMO
      </div>
      <div class="profile_SideBar--body">
        <fa-icon icon="search" class="fa-bodyicon" @click="chkView(0)"> </fa-icon>
        <br>
        최근 조회 API
        <br>
        <fa-icon icon="edit" class="fa-bodyicon" @click="chkView(1)"> </fa-icon>
        <br>
        내가 작성한 게시글
      </div>
  </div>
</template>

<script>
export default {
  name: 'ProfileSideBar',
  data() {
    return {
      userImg : require('@/assets/userimg.png')
    }
  },
  methods: {
    chkView(id) {
      this.$emit('chkViews', id)
    }
  }

}
</script>

<style lang="scss" scope>
  ul {
    list-style: none;
    padding: 0px;
  }
</style>
