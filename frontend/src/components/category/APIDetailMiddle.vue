<template>
<div class="detail">
  <div>
    <div class="detail-Header">
      <h2>사용 방법</h2>
    </div>
  </div>

  <div class="detail-carousel">
    <!-- shuffle btn -->
    <div>
      <span class="btn btn-back" v-show="slideCnt !== 1" @click="slider(false)">
        <fa-icon icon="angle-left"></fa-icon>
      </span>
      <span class="btn btn-go" v-show="slideCnt !== items.length" @click="slider(true)">
        <fa-icon icon="angle-right"></fa-icon>
      </span>
    </div>
    <!-- carousel -->
    <div id="slideImg" style="display:flex;">
      <div v-for="(item, index) in items" :key="index">
        <img :src="imgSrc[index]" alt="">
        <h4>{{ item }}</h4>
        <div><span v-html="howToUse[index]"></span></div>
      </div>
    </div>

  </div>
</div>
</template>

<script>
export default {
  name: 'ApiDetailMiddle',
  data: () => {
    return {
      imgSrc: [require('@/assets/tmdb_1.png'), require('@/assets/tmdb_2.png'), require('@/assets/tmdb_3.png')],
      items: ["1. 회원가입", "2. API Key 요청", "3. API Key 확인"],
      howToUse : [
        " 1-1. <a href='https://www.themoviedb.org/account/signup' alt='TMDB' style='text-decoration:none; color:blue;' target='_blank'>TMDB</a> 사이트 로 접속하여 화원가입 합니다.<br><br> 1-2. 회원가입시 작성한 E-mail로 전송된 E-mail 검증을 완료 합니다. ",
        " 2-1. <b>프로필 => 계정설정</b> 을 클릭합니다. <br><br> 2-2. 좌측 네비게이션에서 <b>API</b>를 클릭하여 API 설정 창으로 이동합니다. <br><br> 2-3. <b>APi Key 요청</b> 란의 <b style='color:#ff567a;'>click here</b>를 눌러 요청 페이지로 이동합니다. <br><br> 2-4. 안내 사항에 따라 작성한 후 API Key 를 발급 받습니다.",
        " 3-1. 요청 받은 API Key를 확인합니다. <br><br> 3-2. API Key의 경우 다른 이에게 공개 되지 않도록 관리합니다."
        ],
      defaultPos: 0,
      slideCnt: 1,
    }
  },
  methods: {
    slider(bool) {
      if (this.slideCnt === this.items.length && bool === true) {return}
      if (this.slideCnt === 1 && bool === false) {return}

      var currentPos = this.defaultPos
      var targetPos

      if (bool) {
        targetPos = currentPos - 600
        this.slideCnt++
      } else {
        targetPos = currentPos + 600
        this.slideCnt--
      }

      var speed = 5
      var elem = document.getElementById('slideImg')

      this.moveSlide(currentPos, targetPos, speed, elem, bool)
      this.defaultPos = targetPos
    },
    moveSlide(cp, tp, speed, elem, dir) {
      if (cp === tp) { return }
      if (dir) {
        cp -= speed
      } else {
        cp += speed
      }
      elem.style.left = cp + 'px'
      setTimeout(() => {
        this.moveSlide(cp, tp, speed, elem, dir)
      }, 1);
    }
  },
}
</script>

<style lang="scss" scoped>
// slide
#slideImg {
  position: relative;
}
.detail-carousel {
  position: relative;
  display: flex;
  overflow: hidden;
}
// img
img {
  // height: 320px;
  height: 450px;
  width: 600px;
  // padding-top: 56.25%;
  margin-right: 10px;
}
h4 {
  margin: {
    left: 10px;
    bottom: 10px;
  }
}
// btn
.btn {
  position: absolute;
  &-back {
    top: 45%;
    z-index: 1;
  }
  &-go {
    top: 45%;
    right: 0%;
    z-index: 1;
  }
}
</style>
