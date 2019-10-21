<template>
  <div class="category">
    <Sidebar :PropData="ApiList"/>
    <div class="category-contents">
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
import Sidebar from "@/components/sidebar"
import APIListCard from "@/components/category/APIListCard"
export default {
  components: {
    APIListCard, Sidebar
  },
  data() {
    return {
      ApiList : [
        {title : 'API LIST'},
        {subtitle : ''},
        {name: '공공데이터'},
        {name: '대중교통'},
        {name: '음악'},
        {name: '영화'},
        {name: '사진'},
        {name: '미디어'},
        {name: '날씨'},
        {name: '영화'},
        {name: '사진'},
        {name: '미디어'},
        {name: '날씨'},
        {name: '영화'},
        {name: '사진'},
        {name: '미디어'},
        {name: '날씨'},
        {name: '영화'},
        {name: '사진'},
        {name: '미디어'},
        {name: '날씨'},
        {name: '영화'},
        {name: '사진'},
        {name: '미디어'},
        {name: '날씨'},
        {name: '영화'},
        {name: '사진'},
        {name: '미디어'},
        {name: '날씨'},
      ]
    }
  }
}
</script>

<style>

</style>
