<template>
<div>
  <div class="divider">
    <h3>Dashboard</h3>
  </div>
  <div class="adminMain">
    <div class="adminMain-card"
      :style="{'background-color': item.color}"
      v-for="item in dataCnt" :key="item.name"
      @click="chartChange(item)"
    >
      <fa-icon class="adminMain-icon" :icon="item.icon"></fa-icon>
      <div class="adminMain-card-text">
        <h2>{{ item.name }}</h2>
        <span>{{ item.count }}</span>
      </div>
    </div>
  </div>

  <div class="adminMain">
    <!-- chart canvas -->
    <BarChart :chartData="chartData" style="width: 600px;"/>

    <div>
      <table class="table-main">
        <h3>Activity</h3>
        <tbody v-for="(active, index) in userActive" :key="index" style="text-align: center;">
          <table class="table-active">
            <tr>
              <th class="table-active table-img" rowspan='2'>
                <img class="userimg" :src="userImg" alt="userimg">
              </th>
              <th><h4>{{ active.id }}</h4><span> {{ active.activity }}</span></th>
            </tr>
            <tr>
              <th class="subText">{{ active.date }}</th>
            </tr>
          </table>
          <div class="separater" v-if="index !== 3"></div>
        </tbody>
      </table>
    </div>
  </div>

  <div class="divider">
    <h3>API</h3>
  </div>

  <div class="adminMain">
    <!-- add -->
    <div v-for="i in 2" :key="i">
      <table class="table-main">

        <thead>
          <h3 v-if="i === 1">New API</h3>
          <h3 v-if="i === 2">Edit API</h3>
          <tr>
            <th v-for="(name, index) in tableName" :key="index">{{ name }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(post, index) in posts" :key="index">
            <th v-for="i in post" :key="i.id">{{ i }}</th>
          </tr>
        </tbody>
      </table>
      <div class="btn btn--primary" @click="goApiList">more<fa-icon class="more-icon" icon="external-link-alt"></fa-icon></div>
    </div>
  </div>
</div>
</template>

<script>
import BarChart from '@/components/BarChart'
export default {
  name: 'AdminMainPage',
  components: {
    BarChart
  },
  data: () => {
    return {
      dataCnt: [
        { name: 'Users', count: 6, collection: { labels: [], data: [0, 0, 2, 3, 1, 0, 0]}, color: '#0090D9', icon: 'user-friends' },
        { name: 'Add Post', count: 15, collection: { labels: [], data: [10, 1, 1, 1, 2, 0, 0]}, color: '#37A8AF', icon: 'calendar-plus' },
        { name: 'Edit Post', count: 32, collection: { labels: [], data: [1, 10, 15, 8, 3, 11, 4]}, color: '#3E739D', icon: 'edit' },
        { name: 'Requests', count: 784, collection: { labels: [], data: [302, 123, 83, 97, 65, 110, 435]}, color: '#f56954', icon: 'project-diagram' },
      ],
      tableName: ['API ID', '제목', '등록일자', '카테고리', '수정요청'],
      posts: [
        { id: 1, title: '오타수정', date: '191020', category: '교통', edit: true },
        { id: 2, title: '오타수정', date: '191021', category: '지도', edit: true },
        { id: 3, title: '오타수정', date: '191021', category: '공공데이터', edit: true },
        { id: 1, title: '업데이트', date: '191022', category: '교통', edit: true },
        { id: 4, title: '업데이트', date: '191023', category: '사진', edit: true },
      ],
      userActive: [
        { id: 'user1', activity: 'create api', date: '191029'},
        { id: 'user2', activity: 'create api', date: '191030'},
        { id: 'user5', activity: 'sign in', date: '191031'},
        { id: 'user6', activity: 'edit api', date: '191101'},
      ],
      userImg : require('@/assets/userimg.png'),
      chartData: {},
    }
  },
  mounted() {
    this.chartData = { data: [40, 20, 30, 50, 90, 10, 20], color: '#f56954'}
    this.userActive.sort(( a, b ) => { return b.date - a.date })
  },
  methods: {
    chartChange(item) {
      this.chartData.color = item.color
      this.chartData.collection = item.collection
    },
    goApiList() {
      this.$router.push({ name: 'AdminPost' })
    }
  }
}
</script>

<style lang="scss" scoped>
h2 {
  margin: {
    top: 40px;
    bottom: 0px;
  }
}
h3 {
  margin: {
    top: 20px;
    left: 20px;
  }
  color: gray;
}
h4 {
  margin: 0;
  display: inline;
  font-size: 20px;
}
span {
  font-weight: 100;
}

.table{
  &-main {
    width: 600px;
    box-shadow: var(--shadow-sm);
    border-radius: 4px;
    border-collapse: collapse;
  }
  &-active {
    text-align: left;
    th {
      margin: 0;
      padding: 0;
    }
    .subText {
      font-size: 14px;
      color: gray;
    }
  }
  &-img {
    height: 70px;
    width: 90px;
    .userimg {
      margin-left: 10px;
      max-width: 70px;
      max-height: 70px;
    }
  }
}

.adminMain {
  display: flex;
  justify-content: space-around;
  &-card {
    display: flex;
    justify-content: space-between;
    position: relative;

    box-shadow: var(--shadow-sm);
    border-radius: 4px;

    margin: {
      bottom: 30px;
    }
    width: 280px;
    height: 140px;
    text-align: center;
    color: white;
    &-text {
      margin: {
        right: 20px;
      }
    }
    &:hover {
      cursor: pointer;
    }
  }
  &-icon {
    font-size: 60px;
    margin: {
      top: 40px;
      left: 20px;
    }
  }
}

.divider {
  margin: 15px 0;
}
.separater {
  display: inline-block;
  margin: {
    top: 5px;
    bottom: 5px;
    // left: 60px;
  }
  width: 500px;
}
.btn {
  float: right;
  margin: {
    top: 10px;
    bottom: 10px;
  }
  .more-icon {
    margin-left: 5px;
  }
}

</style>
