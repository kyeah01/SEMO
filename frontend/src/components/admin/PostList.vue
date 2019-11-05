<template>
<div>
    <div class="test">
      <h1>Admin Post <span class="test-subtext">{{ posts.length }} 개의 api</span></h1>
      <router-link :to="{ name: 'APIWrite' }" class="btn btn--success btn--xl">API 추가</router-link>
    </div>
  <table>
    <thead>
      <tr>
        <th><input type="checkbox" v-model="allSelect" @click="selectAll(true)"></th>
        <th v-for="(name, index) in tableName" :key="index">{{ name }}</th>
      </tr>
    </thead>

    <tbody>
      <tr v-for="(post, index) in paginatedData" :key="index">
        <th><input type="checkbox" :value="post" v-model="checkedPost" @click="selectAll(false)"></th>
        <th v-for="item in post" :key="item">{{ item }}</th>
      </tr>
    </tbody>

  </table>

  <div style="text-align:center;">
    <span @click="paginationBtn(false)" class="btn btn--md" :class="[{'btn--tertiary':pageNum === 0}, 'btn--primary']">prev</span>
    <span v-for="(i, index) in pageCount" :key="index" :class="['pageBtn', {'pageBtn-hl': pageNum === index}]" @click="paginationClick(i)">{{ i }}</span>
    <span @click="paginationBtn(true)" class="btn btn--md" :class="[{'btn--tertiary':pageNum === pageCount-1}, 'btn--primary']">next</span>
  </div>
</div>
</template>

<script>
import { mapGetters } from "vuex"

import router from '@/router'

export default {
  name: 'PostList',
  props: {
    pageSize: {
      type: Number,
      required: false,
      default: 7
    }
  },
  data: () => {
    return {
      tableName: ['API ID', '제목', '등록일자', '카테고리', '요청현황'],
      pageNum: 0,
      checkedPost: [],
      allSelect: false,
      posts: []
    }
  },
  computed: {
    ...mapGetters({
      apiList: 'getApiLists'
    }),
    pageCount () {
      let listLeng = this.posts.length, listSize = this.pageSize, page = Math.floor((listLeng - 1) / listSize) + 1
      return page
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize, end = start + this.pageSize;
      return this.posts.slice(start, end)
    },
  },
  mounted() {
    this.posts = this.setApi()
  },
  methods: {
    paginationBtn (bool) {
      if (bool) {
        if (this.pageCount === this.pageNum+1) {return}
        this.allSelect = false
        this.checkedPost = []
        this.pageNum++
      } else {
        if (this.pageNum === 0) {return}
        this.allSelect = false
        this.checkedPost = []
        this.pageNum--
      }
    },
    paginationClick(i) {
      this.pageNum = i-1
    },
    selectAll(bool) {
      if (bool) {
        if (!this.allSelect) {
          this.checkedPost = this.paginatedData
        } else {
          this.checkedPost = []
        }
      } else {
        this.allSelect = false
      }
    },
    setApi() {
      const apis = this.apiList.map( d => ({
        id: d.id,
        title: d.title,
        date: '191105',
        category: d.tags[0],
        edit: '수락'
      }))
      apis.sort((a, b) => { return b.id - a.id })
      return apis
    },
    test() {
      console.log({ id: 41, title: '대중교통 API', date: '191020', category: '대중교통', edit: "수락" })
    },

  }
}
</script>

<style lang="scss" scoped>
table {
  border-collapse: collapse;
  margin-bottom: var(--space-lg);
  width: 100%;
  height: 600px;
}
th, tr {
  border-bottom: 1px solid rgba(124, 124, 124, 0.479);
}

.btn {
      margin: 0 var(--space-lg);
    }
.pageBtn {
  font-size: 20px;
  margin: 0 var(--space-sm);

  &-hl {
    color: $primary;
    border-bottom: 1px solid $primary;
  }
}
.test-subtext {
  font-size: 16px;
  color: gray;
}
</style>
