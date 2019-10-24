<template>
<div class="detail">
  <div>
    <div class="detail-Header">
      <h2>How to Use</h2>
    </div>
  </div>

  <div class="detail-carousel">
    <!-- shuffle btn -->
    <div>
      <button class="test test-1" @click="slider(false)">back</button>
      <button class="test test-2" @click="slider(true)">go</button>
    </div>
    <!-- carousel -->
    <div id="slideImg" style="display:flex;">
      <div v-for="item in items" :key="item">
        <img :src="imgSrc" alt="">
        <div>{{ item }}</div>
        <div>어딜 보시나요</div>
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
      imgSrc: 'http://toeic.ybmclass.com/toeic/img/noimage.gif',
      items: [1, 2, 3],
      defaultPos: 0,
    }
  },
  methods: {
    slider(bool) {
      var currentPos = this.defaultPos
      var targetPos = currentPos - 500
      var speed = 5
      var elem = document.getElementById('slideImg')

      this.moveLeft(currentPos, targetPos, speed, elem)
      this.defaultPos = targetPos
    },
    moveLeft(cp, tp, speed, elem) {
      if (cp === tp) { return }
      cp -= speed
      elem.style.left = cp + 'px'
      setTimeout(() => {
        this.moveLeft(cp, tp, speed, elem)
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
// img
img {
  height: 320px;
  width: 500px;
  margin-right: 10px;
}

.detail-carousel {
  position: relative;
  display: flex;
  overflow: hidden;
}
.test {
  position: absolute;
  &-1 {
    top: 45%;
    z-index: 1;
  }
  &-2 {
    top: 45%;
    right: 0%;
    z-index: 1;
  }
}
</style>
