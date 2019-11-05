<template>
    <div class="profile_contents--list">
      <h1> 내가 작성한 게시글 </h1>
      <table>
        <thead>
          <tr>
            <th v-for="(name, index) in tableName" :key="index">{{ name }}</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="(post, index) in paginatedData" :key="index" >
            <th v-for="(item, idx) in post" :key="idx">{{ item }}</th>
          </tr>
        </tbody>

      </table>

      <div style="text-align:center;" >
        <span @click="paginationBtn(false)" class="btn btn--md" :class="[{'btn--tertiary':pageNum === 0}, 'btn--primary']">prev</span>
        <span v-for="(i, index) in pageCount" :key="index" :class="['pageBtn', {'pageBtn-hl': pageNum === index}]" @click="paginationClick(i)">{{ i }}</span>
        <span @click="paginationBtn(true)" class="btn btn--md" :class="[{'btn--tertiary':pageNum === pageCount-1}, 'btn--primary']">next</span>
      </div>

  </div>
</template>

<script>
import APIListCard from "@/components/category/APIListCard"
import store from "@/store";
import moment from "moment"

export default {
  name : 'ProfileContents',
  props: {
    pageSize: {
      type: Number,
      required: false,
      default: 7
    }
  },
  data: () => {
    return {
      tableName: ['API ID', '제목', '등록일자', '카테고리', '요청 현황'],
      pageNum: 0,
      checkedPost: [],
      allSelect: false,
      posts: [
        { id: 41, title: '등록테스트', date: '', category: '교통', edit: "수락 대기중" },
        { id: "", title: '', date: '', category: '', edit: "" },
        { id: "", title: '', date: '', category: '', edit: "" },
        { id: "", title: '', date: '', category: '', edit: "" },
        { id: "", title: '', date: '', category: '', edit: "" },
        { id: "", title: '', date: '', category: '', edit: "" },
        { id: "", title: '', date: '', category: '', edit: "" },
      ],
      chkPostData : store.state.postData
    }
  },
  updated() {
    this.chkPostData = store.state.postData
  },
  mounted() {
    this.posts[0].date = moment(new Date()).format('YYYYMMDD')
    if (this.chkPostData === true) {
      this.posts[0].edit = "수락"
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
  }
}
</script>

<style lang="scss" scoped>
table {
  border-collapse: collapse;
  margin-bottom: var(--space-md);
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
