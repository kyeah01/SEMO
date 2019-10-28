<template>
<div>
  <button>add post</button>
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

  <div>
    <span @click="paginationBtn(false)">prev</span>
    <span v-for="(i, index) in pageCount" :key="index" :class="['pageBtn', {'pageBtn-hl': pageNum === index}]">{{ i }}</span>
    <span @click="paginationBtn(true)">next</span>
  </div>
</div>
</template>

<script>
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
      tableName: ['API ID', '제목', '등록일자', '카테고리', '수정요청'],
      pageNum: 0,
      checkedPost: [],
      allSelect: false,
      posts: [
        { id: 1, title: '오타수정', date: '191020', category: '교통', edit: true },
        { id: 2, title: '오타수정', date: '191021', category: '지도', edit: true },
        { id: 3, title: '오타수정', date: '191021', category: '공공데이터', edit: true },
        { id: 1, title: '업데이트', date: '191022', category: '교통', edit: true },
        { id: 4, title: '업데이트', date: '191023', category: '사진', edit: true },
        { id: 5, title: '오타수정', date: '191024', category: '미디어', edit: true },
        { id: 5, title: '업데이트', date: '191024', category: '미디어', edit: true },
        { id: 6, title: '오타수정', date: '191020', category: '교통', edit: true },
        { id: 7, title: '오타수정', date: '191021', category: '지도', edit: true },
        { id: 8, title: '오타수정', date: '191021', category: '공공데이터', edit: true },
        { id: 9, title: '업데이트', date: '191022', category: '교통', edit: true },
        { id: 10, title: '업데이트', date: '191023', category: '사진', edit: true },
        { id: 11, title: '오타수정', date: '191024', category: '미디어', edit: true },
        { id: 32, title: '업데이트', date: '191024', category: '미디어', edit: true },
        { id: 11, title: '오타수정', date: '191020', category: '교통', edit: true },
        { id: 11, title: '오타수정', date: '191021', category: '지도', edit: true },
        { id: 31, title: '오타수정', date: '191021', category: '공공데이터', edit: true },
        { id: 11, title: '업데이트', date: '191022', category: '교통', edit: true },
        { id: 41, title: '업데이트', date: '191023', category: '사진', edit: true },
        { id: 51, title: '오타수정', date: '191024', category: '미디어', edit: true },
        { id: 51, title: '업데이트', date: '191024', category: '미디어', edit: true },
      ]
    }
  },
  computed: {
    pageCount () {
      let listLeng = this.posts.length, listSize = this.pageSize, page = Math.floor((listLeng - 1) / listSize) + 1
      return page
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize, end = start + this.pageSize;
      return this.posts.slice(start, end)
    }
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
    }
  }
}
</script>

<style lang="scss" scoped>
table {
  border-collapse: collapse;
  margin: {
    top: 7%;
  }
  width: 100%;
  height: 600px;
}
th, tr {
  border-bottom: 1px solid rgba(124, 124, 124, 0.479);
}

.pageBtn {
  &-hl {
    border-bottom: 1px solid blue;
  }
}
</style>
