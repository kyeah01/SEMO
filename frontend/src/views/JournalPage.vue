<template>
  <div class="journal">

    <!-- sidebar -->
    <Sidebar>
      <template v-slot:title>
        <h2>{{ developers[0].title }}</h2>
      </template>
      <template v-slot:list>
        <li v-for="item in developers.slice(1, developers.length)" :key="item.name">{{ item.name }}</li>
      </template>
    </Sidebar>

    <!-- content -->
    <div class="journal-contents">
      <div class="journal-contents_head">
        <h2>Journal Page</h2>
      </div>

      <div class="journal-contents_body">
        <table>
          <tr>
            <th>Date</th><th>Title</th>
          </tr>
          <tr v-for=" i in 10" :key="i">
            <td>{{i}}</td><td>a</td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from '@/components/sidebar'

export default {
  components: {
    Sidebar
  },
  data() {
    return{
      developers : [
        {title : "Developers"},
        {name : '김구현'},
        {name : '강예원'},
        {name : '김연주'},
        {name : '박수현'},
        {name : '전영진'},
      ]
    }
  }

}
</script>

<style lang="scss" scope>
.separater {
  margin: 0px;
}
</style>
