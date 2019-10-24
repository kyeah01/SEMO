<template>
<div class="detail">

  <div>
    <div class="detail-Header">
      <h1>Google maps API</h1>
    </div>
    <span class="btn btn--secondary btn-round" v-for="item in tags" :key="item" ><h3>{{ item }}</h3></span>
  </div>

  <div class="detail-Table">
    <div class="detail-Table-left">
      <table v-for="(item, index) in tableTitle[0]" :key="index">
        <thead><h2>{{ item }}</h2></thead>
        <tbody>내용물</tbody>
      </table>
    </div>

    <div class="divider divider-table"></div>

    <div class="detail-Table-right">
      <table v-for="(item, index) in tableTitle[1]" :key="index">
        <thead><h2>{{ item }}</h2></thead>
        <tbody>
          <table class="detail-subTable">
            <tr v-for="(item, subindex) in subTableTitle[index]" :key="subindex">
              <th class="detail-Table-subTitle">{{ item }}</th><th>내용물</th>
            </tr>
          </table>
        </tbody>
      </table>
    </div>
  </div>

</div>
</template>

<script>
export default {
  name: 'ApiDetailTop',
  data: () => {
    return {
      tableTitle: [
        ['API 소개', '주요 기능'],
        ['개요', '가입 및 라이센스']
      ],
      subTableTitle: [
        ['태그', '데이터 형식', 'Protocols', '페이지', '비용 유무'],
        ['로그인', 'KEY 필요유무', '사용료', '서비스 약관']
      ],
      tags: {
        serve: '지도',
        pay: '무료',
        data: 'XML'
      },
    }
  }
}
</script>

<style lang="scss" scoped>
thead, th {
  text-align: left;
}
h3 {
  margin: 0;
}
h2 {
  margin: {
    bottom: 0;
  }
}
</style>
