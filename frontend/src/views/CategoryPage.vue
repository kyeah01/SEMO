<template>
  <div class="category">

    <!-- sidebar -->
    <Sidebar>
      <template v-slot:title>
        <h2>{{ sideBarItems[0].title }}</h2>
      </template>
      <template v-slot:list>
        <li v-for="item in sideBarItems.slice(2, sideBarItems.length)" :key="item.name" @click="formFilter(item.id)">{{ item.name }}</li>
      </template>
    </Sidebar>

    <!-- content -->
    <div class="category-contents">
      <div class="category-list" v-if="!apiLoad">
        <div v-for="item in ApiLists" :key="item.id">
          <APIListCard :item="item" @select="apiSelect"/>
        </div>
      </div>
      <!-- <div class="category-list" v-if="apiLoad">
        <APIDetail :apiId="apiId" @goList="apiLoad = !apiLoad"/>
      </div> -->
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
        {name: '공공데이터', id:1},
        {name: '대중교통', id:2},
        {name: '음악', id:3},
        {name: '영화', id:4},
        {name: '사진', id:5},
        {name: '미디어', id:6},
        {name: '날씨', id:7},
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
        {id: 11, title: 'api'},
        {id: 12, title: 'api'},
        {id: 13, title: 'api'},
        {id: 14, title: 'api'},
        {id: 15, title: 'api'},
        {id: 16, title: 'api'},
        {id: 17, title: 'api'},
        {id: 18, title: 'api'},
        {id: 19, title: 'api'},
        {id: 20, title: 'api'},
        {id: 21, title: 'api'},
        {id: 22, title: 'api'},
        {id: 23, title: 'api'},
        {id: 24, title: 'api'},
        {id: 25, title: 'api'},
        {id: 26, title: 'api'},
        {id: 27, title: 'api'},
        {id: 28, title: 'api'},
        {id: 29, title: 'api'},
        {id: 30, title: 'api'},
        {id: 31, title: 'api'},
        {id: 32, title: 'api'},
        {id: 33, title: 'api'},
        {id: 34, title: 'api'},
        {id: 35, title: 'api'},
        {id: 36, title: 'api'},
        {id: 37, title: 'api'},
        {id: 38, title: 'api'},
        {id: 39, title: 'api'},
        {id: 40, title: 'api'},
      ],
      categoryFilter : 0,
      apiLoad: false,
      apiId: '',
    }
  },
  methods: {
    apiSelect(item) {
      this.apiId = item.id
      this.apiLoad = true
      window.scrollTo(0,0);
      this.$router.push({ name: 'APIDetail', params: { apiId: this.apiId }})
    },
    formFilter(id) {
      this.categoryFilter = id
      console.log(this.categoryFilter)
    }
  }
}
</script>

<style>

</style>
