<template>
  <div class="profile_contents--title">
    <diV>
      <h1 style="font-size:30px;">SEMO's Information</h1>
      <table style="width: 100%;">
        <tr>
          <th><fa-icon icon="user-tie" class="fa-tie"></fa-icon></th>
          <th style="font-size: 30px; width: 30%;">개발자</th>
          <th><fa-icon icon="code" class="fa-tie"></fa-icon></th>
          <th style="font-size: 30px; width: 30%;">파이썬</th>
        </tr>
        <tr>
          <td style="color: grey;">(occupation)</td>
          <td></td>
          <td style="color: grey;">(language)</td>
          <td></td>
        </tr>
      </table>
    </diV>

    <h1 style="font-size:30px;">API Key Storage</h1>
    <div class="profile_keyStorage">
      <div class="profile_keyStorage--select">
        <ul>
          <li>
            <label for="apiCategory">apiCategory</label>
          </li>
          <li>
            <select name="apiCategory" id="apiCategory" v-model="categoryFillter" @change="filter()">
              <option :value="item.id" v-for="(item, index) in apiCategory" :key="index">{{ item.name }}</option>
            </select>
          </li>
        </ul>

        <ul>
          <li>
            <label for="apiList">apiList</label>
          </li>
          <li>
            <select name="apiList" id="apiList" v-model="keyData.detail">
              <option :value="{id:item.fillterid, title:item.title}" v-for="(item, index) in fltList" :key="index" >{{ item.title }}</option>
            </select>
          </li>
        </ul>
      </div>

      <div class="profile_keyStorage--input">
        <ul>
          <li>
            <label for="keyInput">API KEY</label>
          </li>
          <li>
            <input type="text" id="keyInput" v-model="keyData.key" style="width:700px;">
          </li>
        </ul>
        <ul>
          <li>
            <label for="keyValue">Key 만료일</label>
          </li>
          <li>
            <input type="date" id="keyValue" v-model="keyData.date" style="width:200px;">
          </li>
        </ul>
      </div>

      <fa-icon icon="plus" class="btn profile_keyStorage--icon" @click="addAPIKey"> </fa-icon>

    </div>
    <div style="height: 280px;" >
      <table style="width: 100%;" v-if="paginatedData[0]">
        <tr style="font-size: 25px;">
          <th>Category</th>
          <th>API</th>
          <th style="width: 700px;">Key</th>
          <th>Date</th>
        <tr/>
        <tr v-for="(item, index) in paginatedData" :key="index" style="font-size: 20px;">
          <td>{{ apiCategory[item.detail.id].name }}</td>
          <td>{{ item.detail.title }}</td>
          <td style="overflow:auto ; max-width:700px;">{{ item.key }}</td>
          <td>{{ item.date }}</td>
          <fa-icon icon="trash-alt" class="btn" @click="deleteKey(index)"></fa-icon>
        </tr>
      </table>
    </div>
    <div style="height:20px;">
    <div class="profile_pagenation" v-if="pageCount >= 2">
      <span @click="paginationBtn(false)" class="btn btn--md" :class="[{'btn--tertiary':pageNum === 0}, 'btn--primary']">prev</span>
      <span v-for="(i, index) in pageCount" :key="index" class="btn" :class="['pageBtn', {'pageBtn-hl': pageNum === index}]" @click="paginationClick(i)">{{ i }}</span>
      <span @click="paginationBtn(true)" class="btn btn--md" :class="[{'btn--tertiary':pageNum === pageCount-1}, 'btn--primary']">next</span>
    </div>
    </div>

  </div>
</template>

<script>
export default {
 name : 'ProfileUserInfo',
 props: {
    pageSize: {
      type: Number,
      required: false,
      default: 6
    }
  },
 data() {
   return {
      pageNum : 0,
      keyData: {detail: {}, key : "", date: ""},
      userKeyDataList : [],
      ApiLists: [
        {id: 1, title: 'TMDB', fillterid: 4, img:require('@/assets/tmdb.png'), tags:["영화","movie","무료"],body:"영화 정보"},
        {id: 7, title: 'IMDB', fillterid: 4, img:require('@/assets/imdb.png'), tags:["영화","movie","무료"],body:"영화 정보"},
        {id: 8, title: 'Google Maps', fillterid: 2, img:require('@/assets/gmaps.jpg'), tags:["지도","map","무료"],body:"지도 정보"},
        {id: 16, title: 'FaceBook', fillterid: 6, img:require('@/assets/facebook.png'), tags:["Chat BOT","AI","무료"],body:"Facebook ChatBot AI"},
        {id: 17, title: 'Twitter', fillterid: 6, img:require('@/assets/twitter.png'), tags:["SNS","Social","무료"],body:"Twitter 마이크로 블로그 서비스"},
        {id: 18, title: '대중교통 API', fillterid: 2, img:require('@/assets/bus.png'), tags:["대중교통","BUS","무료"],body:"대중교통 길찾기, 버스 정보 등"},
        {id: 19, title: 'Sk T map 교통정보 API', fillterid: 2, img:require('@/assets/sktmap.png'), tags:["교통정보","지도","무료"],body:"T map의 교통정보 API"},
        {id: 20, title: 'Sk T map 경로안내 API', fillterid: 2, img:require('@/assets/sktmap.png'), tags:["교통정보","경로안내","무료"],body:"T map의 경로안내 API"},
        {id: 21, title: '보행자 길찾기 API', fillterid: 2, img:require('@/assets/walk.png'), tags:["교통정보","보행자","무료"],body:"최종 이용자를 원하는 목적지까지 안내하는 API"},
        {id: 33, title: '화물차 경로탐색 API', fillterid: 2, img:require('@/assets/truck.jpg'), tags:["교통정보","보행자","무료"],body:"최종 이용자를 원하는 목적지까지 안내하는 API"},
        {id: 34, title: '자동차 경로탐색 API', fillterid: 2, img:require('@/assets/car.jpg'), tags:["교통정보","보행자","무료"],body:"최종 이용자를 원하는 목적지까지 안내하는 API"},
        {id: 35, title: '한국지도 중국어서비스 API', fillterid: 2, img:require('@/assets/china.png'), tags:["교통정보","보행자","무료"],body:"최종 이용자를 원하는 목적지까지 안내하는 API"},
        {id: 36, title: '한국지도 영어서비스 API', fillterid: 2, img:require('@/assets/america.png'), tags:["교통정보","보행자","무료"],body:"최종 이용자를 원하는 목적지까지 안내하는 API"},
        {id: 37, title: '한국지도 일본어서비스 API', fillterid: 2, img:require('@/assets/japan.png'), tags:["교통정보","보행자","무료"],body:"최종 이용자를 원하는 목적지까지 안내하는 API"},
        {id: 38, title: '올레맵 API', fillterid: 2, img:require('@/assets/alleh.jpg'), tags:["교통정보","보행자","무료"],body:"최종 이용자를 원하는 목적지까지 안내하는 API"},
        {id: 39, title: 'flickr app garden', fillterid: 5, img:require('@/assets/flickr.png'), tags:["교통정보","보행자","무료"],body:"최종 이용자를 원하는 목적지까지 안내하는 API"},
        {id: 40, title: 'nPaint 사진 편집', fillterid: 5, img:require('@/assets/nPaint.png'), tags:["교통정보","보행자","무료"],body:"최종 이용자를 원하는 목적지까지 안내하는 API"},
        {id: 22, title: 'Sony 카메라', fillterid: 5, img:require('@/assets/Sony.png'), tags:["공공데이터","해외통신원","무료"],body:"국제 협력 정보 시스템에서 제공하는 정보"},
        {id: 23, title: 'instagram', fillterid: 5, img:require('@/assets/instagram.png'), tags:["공공데이터","해외통신원","무료"],body:"국제 협력 정보 시스템에서 제공하는 정보"},
        {id: 24, title: 'imgur API', fillterid: 5, img:require('@/assets/imgur.png'), tags:["공공데이터","해외통신원","무료"],body:"국제 협력 정보 시스템에서 제공하는 정보"},
        {id: 9, title: '세계지도 통신', fillterid: 1, img:require('@/assets/seoul.png'), tags:["공공데이터","지식 공유","무료"],body:"세계 도시 통신"},
        {id: 10, title: '수질오염관측정보', fillterid: 1, img:require('@/assets/seoul.png'), tags:["공공데이터","수질","무료"],body:"수질 자동 측정 시스템"},
        {id: 11, title: '공무원 국외 훈련보고', fillterid: 1, img:require('@/assets/seoul.png'), tags:["공공데이터","공무원","무료"],body:"공무원 직무 능력"},
        {id: 12, title: '관용차량 정비이력', fillterid: 1, img:require('@/assets/seoul.png'), tags:["공공데이터","관용차량","무료"],body:"차량 번호별 정비 이력"},
        {id: 13, title: '기술심의 위원 현황', fillterid: 1, img:require('@/assets/seoul.png'), tags:["공공데이터","기술심의","무료"],body:"건설기술심의위원 관련 정보"},
        {id: 14, title: '서울 의료원', fillterid: 1, img:require('@/assets/seoul.png'), tags:["공공데이터","의료","병원"],body:"주간 진료 시간표 현황"},
        {id: 15, title: '국제협력 해외통신원 현황', fillterid: 1, img:require('@/assets/seoul.png'), tags:["공공데이터","해외통신원","무료"],body:"국제 협력 정보 시스템에서 제공하는 정보"},
        {id: 25, title: 'api', fillterid: 1, img:require('@/assets/seoul.png'), tags:["공공데이터","해외통신원","무료"],body:"국제 협력 정보 시스템에서 제공하는 정보"},
        {id: 26, title: 'api', fillterid: 1, img:require('@/assets/seoul.png'), tags:["공공데이터","해외통신원","무료"],body:"국제 협력 정보 시스템에서 제공하는 정보"},
        {id: 27, title: 'api', fillterid: 1, img:require('@/assets/seoul.png'), tags:["공공데이터","해외통신원","무료"],body:"국제 협력 정보 시스템에서 제공하는 정보"},
        {id: 28, title: 'api', fillterid: 1, img:require('@/assets/seoul.png'), tags:["공공데이터","해외통신원","무료"],body:"국제 협력 정보 시스템에서 제공하는 정보"},
        {id: 29, title: 'api', fillterid: 1, img:require('@/assets/seoul.png'), tags:["공공데이터","해외통신원","무료"],body:"국제 협력 정보 시스템에서 제공하는 정보"},
        {id: 30, title: 'api', fillterid: 1, img:require('@/assets/seoul.png'), tags:["공공데이터","해외통신원","무료"],body:"국제 협력 정보 시스템에서 제공하는 정보"},
        {id: 31, title: 'api', fillterid: 1, img:require('@/assets/seoul.png'), tags:["공공데이터","해외통신원","무료"],body:"국제 협력 정보 시스템에서 제공하는 정보"},
        {id: 32, title: 'api', fillterid: 1, img:require('@/assets/seoul.png'), tags:["공공데이터","해외통신원","무료"],body:"국제 협력 정보 시스템에서 제공하는 정보"},
      ],
      userImg : require('@/assets/userimg.png'),
      apiCategory : [
        {name: 'ALL API', id:0},
        {name: '공공데이터', id:1},
        {name: '대중교통', id:2},
        {name: '음악', id:3},
        {name: '영화', id:4},
        {name: '사진', id:5},
        {name: '미디어', id:6},
        {name: '날씨', id:7},
      ],
      categoryFillter : 0,
      fltList : []
   }
 },
mounted() {
  this.fltList = this.ApiLists
},
computed: {
  pageCount () {
    let listLeng = this.userKeyDataList.length, listSize = this.pageSize, page = Math.floor((listLeng - 1) / listSize) + 1
    return page
  },
  paginatedData () {
    const start = this.pageNum * this.pageSize, end = start + this.pageSize;
    return this.userKeyDataList.slice(start, end)
  }
},
 methods: {
   paginationBtn (bool) {
      if (bool) {
        if (this.pageCount === this.pageNum+1) {return}
        this.pageNum++
      } else {
        if (this.pageNum === 0) {return}
        this.pageNum--
      }
    },
    paginationClick(i) {
      this.pageNum = i-1
    },

   filter() {
     if (this.categoryFillter === 0 ) {
      return this.fltList = this.ApiLists
     }
     this.fltList = this.ApiLists.filter(id => id.fillterid === this.categoryFillter)
   },
   addAPIKey() {
     if (this.keyData.detail.id != "" && this.keyData.detail.title != "" && this.keyData.key != "" && this.keyData.date != "") {
      this.userKeyDataList.push(this.keyData)
      this.keyData = {detail:{}, key : "", date: ""}
     }
     else {
       alert("모든 값을 입력 하십시오.")
     }
   },
   deleteKey(index) {
     this.userKeyDataList.splice(index, 1)
   }
 }
}
</script>

<style lang="scss" scope>
.pageBtn {
  &-hl {
    border-bottom: 1px solid blue;
  }
}
</style>
