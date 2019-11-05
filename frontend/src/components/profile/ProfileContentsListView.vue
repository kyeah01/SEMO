<template>
  <div class="profile_contents--list">
      <h1> 최근 조회 API </h1>
      <div class="category-list">
        <div v-for="item in ApiLists" :key="item.id">
          <APIListCard :item="item"/>
        </div>
      </div>
  </div>
</template>

<script>
import APIListCard from "@/components/category/APIListCard"
import store from "@/store"

export default {
  name : 'ProfileContents',
  components: {
    APIListCard
  },
  data() {
   return {
     chkPostData : store.state.postData,
     ApiLists: [
        {id: 1, title: 'TMDB', fillterid: 4, img:require('@/assets/tmdb.png'), tags:["영화","movie","무료"],body:"영화 정보"},
        // {id: 7, title: 'IMDB', fillterid: 4, img:require('@/assets/imdb.png'), tags:["영화","movie","무료"],body:"영화 정보"},
        // {id: 8, title: 'Google Maps', fillterid: 2, img:require('@/assets/gmaps.jpg'), tags:["지도","map","무료"],body:"지도 정보"},
        // {id: 16, title: 'FaceBook', fillterid: 6, img:require('@/assets/facebook.png'), tags:["Chat BOT","AI","무료"],body:"Facebook ChatBot AI"},
        // {id: 17, title: 'Twitter', fillterid: 6, img:require('@/assets/twitter.png'), tags:["SNS","Social","무료"],body:"Twitter 마이크로 블로그 서비스"},
        // {id: 18, title: '대중교통 API', fillterid: 2, img:require('@/assets/bus.png'), tags:["대중교통","BUS","무료"],body:"대중교통 길찾기, 버스 정보 등"},
        // {id: 19, title: 'Sk T map 교통정보 API', fillterid: 2, img:require('@/assets/sktmap.png'), tags:["교통정보","지도","무료"],body:"T map의 교통정보 API"},
        // {id: 20, title: 'Sk T map 경로안내 API', fillterid: 2, img:require('@/assets/sktmap.png'), tags:["교통정보","경로안내","무료"],body:"T map의 경로안내 API"},
        // {id: 21, title: '보행자 길찾기 API', fillterid: 2, img:require('@/assets/walk.png'), tags:["교통정보","보행자","무료"],body:"최종 이용자를 원하는 목적지까지 안내하는 API"},
        // {id: 33, title: '화물차 경로탐색 API', fillterid: 2, img:require('@/assets/truck.jpg'), tags:["교통정보","보행자","무료"],body:"최종 이용자를 원하는 목적지까지 안내하는 API"},
        // {id: 34, title: '자동차 경로탐색 API', fillterid: 2, img:require('@/assets/car.jpg'), tags:["교통정보","보행자","무료"],body:"최종 이용자를 원하는 목적지까지 안내하는 API"},
      ],
   }
 },
  updated() {
    this.chkPostData = store.state.postData
  },
  mounted() {
    if (this.chkPostData === true) {
      this.ApiLists.push({id: 41, title: '등록테스트', fillterid: 1, img:'http://toeic.ybmclass.com/toeic/img/noimage.gif', tags:["영화","movie","무료"],body:"영화 정보"})
    }
  },
}
</script>

<style>

</style>
