<template>
<div class="detail">

  <div>
    <div class="detail-Header">
      <h1>등록테스트</h1>
    </div>
    <span class="btn btn-round" :class="item.btnClass" v-for="item in tags" :key="item.idx" ><h3>{{ item.name }}</h3></span>
  </div>

  <div class="detail-Table">
    <div class="detail-Table-left">
      <table v-for="(item, index) in tableTitle[0]" :key="index">
        <thead><h2>{{ item.title }}</h2></thead>
        <tr v-for="list in item.contents" :key="list"><li> {{ list }} </li></tr>
      </table>
    </div>

    <div class="divider divider-table"></div>

    <div class="detail-Table-right">
      <table v-for="(item, index) in tableTitle[1]" :key="index">
        <thead><h2>{{ item }}</h2></thead>
        <tbody>
          <table class="detail-subTable">
            <tr v-for="(item, subindex) in subTableTitle[index]" :key="subindex">
              <th class="detail-Table-subTitle"> <h3>{{ item.title }}</h3></th> <th> <a :href="item.contents" v-if="item.chkLink" style="text-decoration: none;" target="_blank"> {{ item.contents }} </a> <span v-else> {{ item.contents }} </span></th>
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
  name: 'ApiDetailTopT',
  data: () => {
    return {
      tableTitle: [
        [
          {title : 'API 소개', contents: ["등록테스트"]},
          {title : '주요 기능', contents: ["등록테스트"]}
        ],
        ['개요', '가입 및 라이센스']
      ],
      subTableTitle: [
        [
          {title: '태그', contents: "공공데이터"},
          {title: '데이터 형식', contents: "JSON, JSONP, KML"},
          {title: 'Protocols', contents: "HTTP, REST, XMPP"},
          {title: '페이지', contents: "", chkLink:true},
          {title: '비용 유무', contents: "무료"}
        ],
        [
          {title: '로그인', contents: "YES"},
          {title: 'KEY 필요유무', contents: "YES"},
          {title: '사용료', contents: "", chkLink:true},
          {title: '서비스 약관', contents: "", chkLink:true}
        ]
      ],
      tags: [
        {idx : 0, name: '공공데이터', btnClass: "btn--primary"},
        {idx : 1, name: '무료', btnClass: "btn--success"},
        {idx : 2, name: 'XML', btnClass: "btn--warning"}
      ],
    }
  },
  methods: {
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
