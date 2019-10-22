<template>
  <div class="category">
    <Sidebar :PropData="sideBarItems"/>
    <div>
      <p>API Category</p>
      <div class="category-list">
          <div v-for="item in ApiLists" :key="item.id">
            <APIListCard :item="item"/>
          </div>
      </div>
      </div>
  </div>
</template>

<script>
import Sidebar from "@/components/sidebar"
import APIListCard from "@/components/category/APIListCard"

export default {
  name: 'CategoryPage',
  components: {
    APIListCard, Sidebar
  },
  data() {
    return {
      sideBarItems : [
        {title : 'API LIST'},
        {subtitle : ''},
        {name: '공공데이터'},
        {name: '대중교통'},
        {name: '음악'},
        {name: '영화'},
        {name: '사진'},
        {name: '미디어'},
        {name: '날씨'},
      ],
      ApiLists: [
        {id: 1, title: 'api'},
        {id: 2, title: 'api'},
        {id: 3, title: 'api'},
        {id: 4, title: 'api'},
        {id: 5, title: 'api'},
      ]
    }
  }
}
</script>

<style>

</style>
