<template>
  <div class="category">
    <Sidebar :PropData="sideBarItems"/>
    <div class="category-contents">
      <div class="category-list" v-if="!apiLoad">
        <div v-for="item in ApiLists" :key="item.id">
          <APIListCard :item="item" @select="apiSelect"/>
        </div>
      </div>
      <div class="category-list" v-if="apiLoad">
        <APIDetail :apiId="apiId" @goList="apiLoad = !apiLoad"/>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "@/components/sidebar"
import APIListCard from "@/components/category/APIListCard"
import APIDetail from "@/components/category/APIDetail"

export default {
  name: 'CategoryPage',
  components: {
    Sidebar,
    APIListCard,
    APIDetail,
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
        {id: 6, title: 'api'},
        {id: 7, title: 'api'},
        {id: 8, title: 'api'},
        {id: 9, title: 'api'},
        {id: 10, title: 'api'},
      ],
      apiLoad: false,
      apiId: '',
    }
  },
  methods: {
    apiSelect(item) {
      this.apiId = item.id
      this.apiLoad = true
    }
  }
}
</script>

<style>

</style>
