<template>
<div>

  <div class="adminMain">
    <div class="adminMain-card" :style="{'background-color': item.color}" v-for="item in dataCnt" :key="item.name">
      <fa-icon class="adminMain-icon" :icon="item.icon"></fa-icon>
      <div class="adminMain-card-text">
        <h2>{{ item.name }}</h2>
        <span>{{ item.count }}</span>
      </div>
    </div>
  </div>

  <div class="adminMain">
    <div>그래프</div>
    <div>게시판</div>
  </div>

  <div class="adminMain">
    <!-- add -->
    <div v-for="i in 2" :key="i">
      <table>
        <thead>
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
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'AdminMainPage',
  data: () => {
    return {
      dataCnt: [
        { name: 'Users', count: 139, color: '#0090D9', icon: 'user-friends' },
        { name: 'Add Post', count: 256, color: '#37A8AF', icon: 'calendar-plus' },
        { name: 'Edit Post', count: 76, color: '#3E739D', icon: 'edit' },
        { name: 'Requests', count: 784, color: '#f56954', icon: 'project-diagram' },
      ],
      tableName: ['API ID', '제목', '등록일자', '카테고리', '수정요청'],
      posts: [
        { id: 1, title: '오타수정', date: '191020', category: '교통', edit: true },
        { id: 2, title: '오타수정', date: '191021', category: '지도', edit: true },
        { id: 3, title: '오타수정', date: '191021', category: '공공데이터', edit: true },
        { id: 1, title: '업데이트', date: '191022', category: '교통', edit: true },
        { id: 4, title: '업데이트', date: '191023', category: '사진', edit: true },
      ],
    }
  }
}
</script>

<style lang="scss" scoped>
.adminMain {
  display: flex;
  justify-content: space-around;
  &-card {
    display: flex;
    justify-content: space-between;
    position: relative;

    box-shadow: var(--shadow-sm);

    margin: {
      top: 30px;
      bottom: 30px;
    }
    width: 280px;
    height: 140px;
    text-align: center;
    color: white;
    h2 {
      margin: {
        top: 40px;
        bottom: 0px;
      }
    }
    &-text {
      margin: {
        right: 20px;
      }
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
</style>
