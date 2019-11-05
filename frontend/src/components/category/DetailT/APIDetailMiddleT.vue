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
  name: 'ApiDetailMiddleT',
  data: () => {
    return {
      imgSrc: [require('@/assets/ssafy.png')],
      items: ["1. 등록테스트"],
      howToUse : ["등록테스트"],
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
