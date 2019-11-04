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
      <div v-for="(item, index) in items" :key="index" style="position: relative;">
        <img v-if="item.imgSrc === false" :src="imgSrc" alt="examImage">
        <img v-else :src="item.imgSrc" alt="uploadImage">

        <label v-if="edit" for="input_file"></label>
        <input v-if="edit" type="file" id="input_file" class="upload-hidden" @click="findIndex(index)" @change="uploadImage">
        <h4>{{ index + 1 }}</h4>
        <div>
          <li v-if="!edit">{{ item.contents }}</li>
          <textarea v-else
            v-model="item.contents" :placeholder="item.placeholder"
            cols="75" rows="18" style="resize: none;"></textarea>
        </div>
      </div>
      <div v-if="edit">
        <fa-icon icon="plus" class="btn" style="font-size: 50px; top: 200px; right: -90px;" @click="plusItem()"></fa-icon>
      </div>
    </div>
  </div>
  <div style="position: absolute; right: -200px; top: 370px; font-size: 50px;">
    <div>
      <fa-icon v-if="edit" :icon="['far', 'check-square']" style="z-index: 2;" @click="edit = !edit"></fa-icon>
      <fa-icon v-else icon="check-square" style="z-index: 2;" @click="edit = !edit"></fa-icon>
    </div>
    <div>
       <fa-icon icon="window-close" style="z-index: 2;"></fa-icon>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'ApiWriteMiddle',
  data: () => {
    return {
      imgSrc: 'http://toeic.ybmclass.com/toeic/img/noimage.gif',
      items: [
        { imgSrc: false, contents: '', placeholder: '사용 방법을 자세하게 입력해주세요.'},
      ],
      defaultPos: 0,
      slideCnt: 1,
      edit: true,
      uploadIndex: 0,
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
    },
    findIndex(index) {
      this.uploadIndex = index
    },
    uploadImage(file) {
      let loadFile = file.target.files || file.dataTransfer.files
      if (loadFile.length == 0) {
          return
      }
      this.addViewImage(loadFile[0])
    },
    addViewImage(file) {
      let reader = new FileReader()
      if ( !file.type.match(/image.*/) ) {
        alert('이미지 파일만 올려주세요.')
        return
      }
      reader.onload = (event) => {
        this.items[this.uploadIndex].imgSrc = event.target.result
      }
      reader.readAsDataURL(file)
    },
    plusItem() {
      this.items.push({ imgSrc: false, contents: '', placeholder: '사용 방법을 자세하게 입력해주세요.'})
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
.upload-hidden {
  // border: 1px solid red;
  position: absolute;
  left: 0px;
  height: 450px;
  width: 600px;
}
label {
  cursor: pointer;
}
input[type="file"] {
  opacity: 0;
}
textarea {
  margin-left: 30px;
}
</style>
