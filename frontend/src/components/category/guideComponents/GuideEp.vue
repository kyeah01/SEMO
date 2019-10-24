<template>
<div>
  <div>
    1. EndPoint
  </div>
  <div class="Guide-ep-content">
    <!-- 왼쪽 테이블 -->
    <table class="Guide-ep-table">
      <thead>
        <tr>
          <th><h3>ENDPOINT</h3></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in endPoint" :key="item">
          <th :class="[{ 'select-Ep-act' : is_activeEp === index }, 'select-Ep']" @click="epSelect(index)"><h3>{{ item }}</h3></th>
        </tr>
      </tbody>
    </table>
    <!-- 오른쪽 테이블 -->
    <table class="Guide-ep-subTable">
      <thead>
        <tr>
          <th :class="[{ 'select-Lang-act' : is_activeLang === index }, 'select-Lang']" v-for="(item, index) in lang" :key="index" @click="langSelect(index)"><h3>{{ item.title }}</h3></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th class="Guide-ep-inputBox" colspan="8">
            {{ displayCode }}
          </th>
        </tr>
      </tbody>
    </table>
  </div>
</div>
</template>

<script>
export default {
  name: 'APIGuideEp',
  data: () => {
    return {
      // props
      endPoint: ['POST', 'PUT', 'DELETE', 'GET'],
      // 고정값
      lang: [
        {
          title: 'JAVA',
          code: 'JAVA reponse = Uniset.GET("")'
        },
        {
          title: 'PYTHON',
          code: 'PYTHON reponse = Uniset.GET("")'
        },
        {
          title: 'NODE',
          code: 'NODE reponse = Uniset.GET("")'
        },
        {
          title: 'RUBY',
          code: 'RUBY reponse = Uniset.GET("")'
        },
        {
          title: 'PHP',
          code: 'PHP reponse = Uniset.GET("")'
        },
        {
          title: 'OBJ-C',
          code: 'OBJ-C reponse = Uniset.GET("")'
        },
        {
          title: '.NET',
          code: '.NET reponse = Uniset.GET("")'
        },
        {
          title: 'CURL',
          code: 'CURL reponse = Uniset.GET("")'
        }
      ],
      displayCode: '',
      is_activeEp: 0,
      is_activeLang: 0,
    }
  },
  mounted() {
    this.displayCode = this.lang[0].code
  },
  methods: {
    epSelect(id) {
      if (id === this.is_activeEp) {return}
      this.is_activeEp = id
    },
    langSelect(id) {
      if (id === this.is_activeLang) {return}
      this.is_activeLang = id
      this.displayCode = this.lang[id].code
    }
  }
}
</script>

<style lang="scss" scoped>
div {
  border: 1px solid blue;
}
.Guide-ep {
  &-content {
    position: relative;
    display: flex;
  }
  &-table {
    th {
      width: 200px;
    }
  }
  &-subTable {
    width: 100%;
    th {
      width: 200px;
    }
    .Guide-ep-inputBox {
      height: 500px;
    }
  }
}
// color
.select {
  &-Ep {
    border-left: 4px solid transparent;
    &-act {
      border-left: 4px solid blue;
    }
  }
  &-Lang {
    border-bottom: 4px solid transparent;
    &-act {
      border-bottom: 4px solid blue
    }
  }
}
</style>
