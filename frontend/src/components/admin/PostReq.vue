<template>
<div>
    <div class="test">
      <h1>API add request</h1>
      <div>
        <span class="btn btn--success btn--xl" @click="dinedAPI(false)">API 수락</span>
        <span class="btn btn--danger btn--xl" @click="dinedAPI(true)">API 거절</span>
      </div>
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
import moment from "moment"

export default {
  name: 'PostReq',
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
      posts: [
        { id: 41, title: '등록테스트', date: moment(new Date()).format('YYMMDD'), category: '공공데이터', edit: "요청대기중" },
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
    dinedAPI(bool) {
      if (bool) {
        this.posts = []
      } else {
        this.$store.commit('setNewApi', this.posts[0])
        this.posts = []
      }
    }
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
</style>
