<template>
<div class="detail">

  <div>
    <div class="detail-Header">
      <h1>The Movie DataBase API</h1>
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
  name: 'ApiDetailTop',
  data: () => {
    return {
      tableTitle: [
        [
          {title : 'API 소개', contents: ["영화 데이터베이스 (TMDb)는 커뮤니티 제작 영화 및 TV 데이터베이스입니다. 모든 데이터는 2008 년으로 거슬러 올라가는 놀라운 커뮤니티에 의해 추가되었습니다. TMDb의 강력한 국제적 초점 과 광범위한 데이터는 비교할 수없는 수준이며 우리가 자랑스럽게 생각하는 것입니다. 간단히 말해서, 우리는 지역 사회에 살고 숨 쉬며 이것이 바로 우리를 다르게 만듭니다."]},
          {title : '주요 기능', contents: ["최고 평점 영화", "인기 영화", "최고 평점 TV 프로그램", "인기있는 배우"]}
        ],
        ['개요', '가입 및 라이센스']
      ],
      subTableTitle: [
        [
          {title: '태그', contents: "#영화, #movie, #tmdb"},
          {title: '데이터 형식', contents: "XML, JSON, VML, KML"},
          {title: 'Protocols', contents: "JavaScript"},
          {title: '페이지', contents: "https://developers.themoviedb.org/3/getting-started/introduction", chkLink:true},
          {title: '비용 유무', contents: "무료"}
        ],
        [
          {title: '로그인', contents: "YES"},
          {title: 'KEY 필요유무', contents: "YES"},
          {title: '사용료', contents: "", chkLink:true},
          {title: '서비스 약관', contents: "https://www.themoviedb.org/terms-of-use", chkLink:true}
        ]
      ],
      tags: [
        {idx : 0, name: '영화', btnClass: "btn--primary"},
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
