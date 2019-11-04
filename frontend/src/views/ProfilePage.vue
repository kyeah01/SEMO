<template>
  <div class="profile">
    <ProfileSideBar @chkViews="chkView"/>
    <div class="profile_contents">
      <ProfileUserInfo/>
      <transition name="fade" mode="out-in">
        <ProfileContentsListView  v-if="toggleViews===0"/>
        <ProfileContentsListPost  v-if="toggleViews===1"/>
      </transition>
    </div>
  </div>
</template>

<script>
import ProfileSideBar from '@/components/profile/ProfileSideBar'
import ProfileContentsListView from '@/components/profile/ProfileContentsListView'
import ProfileContentsListPost from '@/components/profile/ProfileContentsListPost'
import ProfileUserInfo from '@/components/profile/ProfileUserInfo'


export default {
 name : 'ProfilePage',
 components: {
   ProfileSideBar,
   ProfileContentsListView,
   ProfileContentsListPost,
   ProfileUserInfo,
 },
 data() {
   return {
    toggleViews : 0
   }
 },
 methods: {
   chkView(id) {
     this.toggleViews = id
   }
 }

}
</script>

<style>

</style>
