<template>
  <div class="profile">
    <ProfileSideBar @chkViews="chkView"/>
    <div class="profile_contents">
      <ProfileUserInfo/>

      <ProfileContents :toggleViews="toggleViews"/>
    </div>
  </div>
</template>

<script>
import ProfileSideBar from '@/components/profile/ProfileSideBar'
import ProfileContents from '@/components/profile/ProfileContents'
import ProfileUserInfo from '@/components/profile/ProfileUserInfo'


export default {
 name : 'ProfilePage',
 components: {
   ProfileSideBar,
   ProfileContents,
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
