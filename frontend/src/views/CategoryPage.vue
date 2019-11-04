<template>
  <div class="category">

    <!-- sidebar -->
    <Sidebar>
      <template v-slot:title>
        <h2 style="cursor:pointer;" @click="formFilter(0,'API LIST')">{{ sideBarItems[0].title }}</h2>
      </template>
      <template v-slot:list>
        <li v-for="item in sideBarItems.slice(2, sideBarItems.length)" :key="item.name" @click="formFilter(item.id, item.name)">{{ item.name }}</li>
      </template>
    </Sidebar>

    <!-- content -->
    <div class="category-contents">
      <h1>{{ categoryFilterName }}</h1>
      <div class="category-list" v-if="!apiLoad">
        <div v-for="item in ApiLists.slice().reverse()" :key="item.id">
          <APIListCard :item="item" @select="apiSelect" v-if="categoryFilter===0"/>
          <APIListCard :item="item" @select="apiSelect" v-if="categoryFilter===item.fillterid"/>
        </div>
      </div>
      <!-- <div class="category-list" v-if="apiLoad">
        <APIDetail :apiId="apiId" @goList="apiLoad = !apiLoad"/>
      </div> -->
    </div>
  </div>
</template>

<script>
import Sidebar from "@/components/sidebar"
import APIListCard from "@/components/category/APIListCard"
import APIDetail from "@/components/category/APIDetail"

export default {
  name: 'CategoryPage',
  components: {
    Sidebar,
    APIListCard,
    APIDetail,
  },
  data() {
    return {
      sideBarItems : [
        {title : 'API LIST'},
        {subtitle : ''},
        {name: '공공데이터', id:1},
        {name: '대중교통', id:2},
        {name: '음악', id:3},
        {name: '영화', id:4},
        {name: '사진', id:5},
        {name: '미디어', id:6},
        {name: '날씨', id:7},
      ],
      ApiLists: [
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
        {id: 17, title: 'Twitter', fillterid: 6, img:require('@/assets/twitter.png'), tags:["SNS","Social","무료"],body:"Twitter 마이크로 블로그 서비스"},
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
        {id: 8, title: 'Google Maps', fillterid: 2, img:require('@/assets/gmaps.jpg'), tags:["지도","map","무료"],body:"지도 정보"},
        {id: 18, title: '대중교통 API', fillterid: 2, img:require('@/assets/bus.png'), tags:["대중교통","BUS","무료"],body:"대중교통 길찾기, 버스 정보 등"},
        {id: 16, title: 'FaceBook', fillterid: 6, img:require('@/assets/facebook.png'), tags:["Chat BOT","AI","무료"],body:"Facebook ChatBot AI"},
        {id: 7, title: 'IMDB', fillterid: 4, img:require('@/assets/imdb.png'), tags:["영화","movie","무료"],body:"영화 정보"},
        {id: 1, title: 'TMDB', fillterid: 4, img:require('@/assets/tmdb.png'), tags:["영화","movie","무료"],body:"영화 정보"},
      ],
      categoryFilter : 0,
      categoryFilterName : "API LIST",
      apiLoad: false,
      apiId: '',
    }
  },
  computed: {

  },
  methods: {
    apiSelect(item) {
      this.apiId = item.id
      this.apiLoad = true
      window.scrollTo(0,0);
      this.$router.push({ name: 'APIDetail', params: { apiId: this.apiId }})
    },
    formFilter(id, name) {
      this.categoryFilterName = name
      this.categoryFilter = id
    }
  },
}
</script>

<style>

</style>
