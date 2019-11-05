<template>
<div class="detail">

  <div>
    <div class="detail-Header" style="position: relative;">
      <h1 v-if="!apiData.title.hold"><input class="input input-title" type="text" v-model="apiData.title.text" :placeholder="apiData.title.placeholder" style="font-size:25px;"></h1>
      <h1 v-else>{{ apiData.title.text }}</h1>
    </div>
    <span class="btn btn-round"
      v-for="item in apiData.tags" v-show="item.name" :class="item.btnClass" :key="item.idx"
      >
      <h3>{{ item.name }}</h3>
    </span>
  </div>

  <div class="detail-Table">
    <!-- 텍스트 소개 -->
    <div class="detail-Table-left" v-if="!apiData.title.hold">
      <table v-for="(item, index) in apiData.tableTitle[0]" :key="index">
        <thead><h2>{{ item.title }}</h2></thead>
        <tr v-if="index === 0"><textarea class="input-css" cols="68" rows="18" v-model="item.contents[0]" :placeholder="item.placeholder" style="resize: none;"></textarea></tr>
        <tr v-if="index === 1">
          <li v-for="(i, index) in item.leng" :key="i"><input class="input-leftTable input-css" type="text" v-model="item.contents[index]" :placeholder="item.placeholder"></li>
          <fa-icon icon="plus" class="btn" style="top: 10px; left: 230px;" @click="plusTable(item)"></fa-icon>
        </tr>
      </table>
    </div>

    <div class="detail-Table-left" v-else>
       <table v-for="(item, index) in apiData.tableTitle[0]" :key="index">
        <thead><h2>{{ item.title }}</h2></thead>
        <tr v-for="list in item.contents" :key="list"><li> {{ list }} </li></tr>
      </table>
    </div>

    <div class="divider divider-table"></div>
    <!-- 테이블 소개 -->
    <div class="detail-Table-right" v-if="!apiData.title.hold">
      <table v-for="(item, index) in apiData.tableTitle[1]" :key="index">
        <thead><h2>{{ item }}</h2></thead>
        <tbody>
          <table class="detail-subTable">
            <tr v-for="(item, subindex) in apiData.subTableTitle[index]" :key="subindex">
              <th class="detail-Table-subTitle">
                <h3>{{ item.title }}</h3>
              </th>
              <th style="height: 53px;">
                <span :href="item.contents" v-if="item.chkLink"><input class="input input-href" type="text" :placeholder="item.placeholder"></span>
                <span v-else-if="item.chkBool === true">
                  <multiselect
                    v-model="item.contents" :options="item.options" :searchable="false"
                    :close-on-select="false" :show-labels="false" placeholder="선택해주세요"
                    style="width: 480px;"></multiselect>
                </span>
                <span v-else-if="item.chkBool === false">
                  <multiselect
                    v-model="item.contents" :options="item.options" :searchable="false"
                    :close-on-select="false" :show-labels="false" :multiple="true"
                    placeholder="선택해주세요"
                    style="width: 480px;"></multiselect>
                </span>
                <span v-else> {{ item.contents }} </span>
              </th>
            </tr>
          </table>
        </tbody>
      </table>
    </div>

    <div class="detail-Table-right" v-else>
      <table v-for="(item, index) in apiData.tableTitle[1]" :key="index">
        <thead><h2>{{ item }}</h2></thead>
        <tbody>
          <table class="detail-subTable">
            <tr v-for="(item, subindex) in apiData.subTableTitle[index]" :key="subindex">
              <th class="detail-Table-subTitle"> <h3>{{ item.title }}</h3></th>
              <th>
                <a :href="item.contents" v-if="item.chkLink" style="text-decoration: none;" target="_blank">{{ item.contents }}</a>
                <span v-else-if="typeof(item.contents) === 'object'" v-for="(i, index) in item.contents" :key="i">
                  <span v-if="index !== item.contents.length - 1">{{ i }},&nbsp;</span>
                  <span v-else >{{ i }}</span>
                </span>
                <span v-else>{{ item.contents }}</span>
              </th>
            </tr>
          </table>
        </tbody>
      </table>
    </div>
  </div>
  <div style="position: absolute; right: -200px; top: 370px; font-size: 50px;">
    <div>
      <fa-icon v-if="!apiData.title.hold" :icon="['far', 'check-square']" style="z-index: 2;" @click="holdText(true, apiData.title)"></fa-icon>
      <fa-icon v-else icon="check-square" style="z-index: 2;" @click="holdText(false, apiData.title)"></fa-icon>
    </div>
    <div>
       <fa-icon icon="window-close" style="z-index: 2;"></fa-icon>
    </div>
  </div>
</div>
</template>

<script>
import Multiselect from 'vue-multiselect'

export default {
  name: 'ApiWriteTop',
  components: {
    Multiselect
  },
  data: () => {
    return {
      apiData: {
        title: {
          placeholder: 'API title',
          hold: false,
          text: '',
        },
        tableTitle: [
          [
            {title : 'API 소개', contents: [''], placeholder: 'API에 대한 소개를 입력해주세요.'},
            {title : '주요 기능', contents: [], placeholder: '주요 기능을 간략하게 입력해주세요.', leng: 1}
          ],
          ['개요', '가입 및 라이센스']
        ],
        subTableTitle: [
          [
            {title: '태그', contents: "", options: ['공공데이터', '대중교통','음악', '영화', '사진', '미디어', '날씨'], chkBool: true},
            {title: '데이터 형식', contents: [], options: ['JSON', 'JSONP', 'XML', 'VML', 'KML', 'RSS', 'Atom', 'Text', 'None'], chkBool: false},
            {title: 'Protocols', contents: [], options: ['HTTP', 'REST', 'XMPP', 'SOAP', 'Flash', 'None'], chkBool: false},
            {title: '페이지', contents: "", chkLink:true, placeholder: '값을 입력해주세요.'},
            {title: '비용 유무', contents: "", options: ['무료', '유료'], chkBool: true}
          ],
          [
            {title: '로그인', contents: "", options: ['YES', 'NO'], chkBool: true},
            {title: 'KEY 필요유무', contents: "", options: ['YES', 'NO'], chkBool: true},
            {title: '사용료', contents: "", chkLink:true, placeholder: '값을 입력해주세요.'},
            {title: '서비스 약관', contents: "", chkLink:true, placeholder: '값을 입력해주세요.'}
          ]
        ],
        tags: [
          {idx : 0, name: '', btnClass: "btn--primary"},
          {idx : 1, name: '', btnClass: "btn--success"},
          {idx : 2, name: '', btnClass: "btn--warning"}
        ],
      },
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
        {idx : 0, name: '지도', btnClass: "btn--primary"},
        {idx : 1, name: '무료', btnClass: "btn--success"},
        {idx : 2, name: 'XML', btnClass: "btn--warning"}
      ],
    }
  },
  watch: {
    apiData: {
      deep: true,
      handler() {
        this.apiData.tags[0].name = this.apiData.subTableTitle[0][0].contents
        this.apiData.tags[1].name = this.apiData.subTableTitle[0][4].contents
        this.apiData.tags[2].name = this.apiData.subTableTitle[0][1].contents[0]
      }
    }
  },
  methods: {
    holdText(bool, section){
      if (bool && section.text) {
        section.hold = true
      } else {
        section.hold = false
      }
    },
    plusTable(section) {
      section.leng += 1
    }
  }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

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

.input {
  border: {
    top: 0px;
    left: 0px;
    right: 0px;
  }
  &-title {
    line-height: 30px;
  }
  &-leftTable {
    width: 470px;
  }
  &-href {
    line-height: 20px;
    width: 473px;
    height: 32px;
    padding: {
      top: 6px;
      left: 8px;
    }
    border-radius: 5px;
    font-size: 16px;
    &::placeholder {
      font-size: 16px;
    }
  }
}
.input-css {
  border: {
    top: 0;
    left: 0;
    right: 0;
  }
}
</style>
