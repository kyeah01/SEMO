<template>
  <div class="category">
    <sidebar>
      API LIST
      <div class="separater"></div>
      <ul>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
      </ul>
    </sidebar>
    <div>
      <p>API Category</p>
      <div class="category-list">
          <div v-for="item in 10" :key="item">
            <APIListCard/>
          </div>
      </div>
      </div>

  </div>
</template>

<script>
import APIListCard from "@/components/category/APIListCard"
export default {
  components: {
    APIListCard
  }
}
</script>

<style>

</style>
