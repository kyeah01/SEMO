<template>
<div class="admin-main">
  <Sidebar :PropData="sideBarItems"/>
  <div class="admin-contents">
    <div>
      <router-link :to="{ name: 'AdminPost' }">post</router-link>
      <transition name="fade" mode="out-in">
        <router-view/>
      </transition>
    </div>
  </div>
</div>
</template>

<script>
import Sidebar from "@/components/sidebar"

export default {
  name: 'AdminPage',
  components: {
    Sidebar,
  },
  data: () => {
    return {
      sideBarItems : [
        {title : 'Admin'},
        {subtitle : ''},
        {name: 'posts'},
      ],
      topCardItems: [
        { name: 'Api', count: 2064 },
        { name: 'Users', count: 1738 },
        { name: 'Page Views', count: 5965 },
        { name: 'Rate', count: 10 },
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
div {
  // border: 1px solid red;
}
.admin {
  &-main {
    display: flex;
  }
  &-contents {
    margin: {
      top: var(--space-md);
      left: 270px;
      right: 200px;
    }
    width: 100%;
    height: 800px;
    position: relative;
    text-align: start;
    background-color: white;
    box-shadow: var(--shadow-sm);
  }

  &-list {
    display: flex;
    flex-wrap: wrap;
  }
}
</style>
