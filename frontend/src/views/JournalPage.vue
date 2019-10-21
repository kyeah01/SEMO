<template>
  <div class="journal">
    <Sidebar :PropData="developers"/>
    <div class="journal-contents">
      <div class="journal-contents_head">
        <h2>journalPage</h2>
      </div>
      <div class="journal-contents_body">
        <table>
          <tr>
            <th>a</th><th>a</th><th>s</th><th>s</th>
          </tr>
          <tr>
            <td>a</td><td>a</td><td>a</td><td>a</td>
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
