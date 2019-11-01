<template>
<div class="admin-main">
  <!-- sidebar -->
  <Sidebar>
    <template v-slot:title>
      <h2>{{ sideBarItems[0].title }}</h2>
    </template>
    <template v-slot:list>
      <router-link v-for="route in routes[routes.length - 1].children" :key="route.path" :to="{name: route.name}">
        {{ route.name }}
      </router-link>
    </template>
  </Sidebar>
  <!-- content -->
  <div class="admin-contents">
    <div>
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
  },
  computed: {
    routes() {
      console.log(this.$router.options.routes);

      return this.$router.options.routes
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
      bottom: var(--space-md);
      left: 270px;
      right: 200px;
    }
    width: 100%;
    min-height: 800px;
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
