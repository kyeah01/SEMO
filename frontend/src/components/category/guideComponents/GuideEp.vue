<template>
<div>
  <div>
    <h2>1. EndPoint</h2>
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
        <tr v-for="(item, index) in endPoint" :key="index">
          <th :class="[{ 'select-Ep-act' : is_activeEp === index }, 'select-Ep']" @click="epSelect(index)">
            <h3>
              <span class="btn" :class="{'btn--success' : item.methods == 'POST', 'btn--primary' : item.methods == 'GET' , 'btn--danger' : item.methods == 'DELETE', 'btn--warning' : item.methods == 'PUT'  }">{{ item.methods }}</span>
              <br>
              {{ item.contents }}
            </h3>
          </th>
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
            <pre style="font-size:18px; user-select: text;" v-if="is_activeLang===0">
var data = "{}";

var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function () {
  if (this.readyState === this.DONE) {
    console.log(this.responseText);
  }
});

xhr.open("GET", "https://api.themoviedb.org/3/movie/%7Bmovie_id%7D?language=en-US&api_key=%3C%3Capi_key%3E%3E");

xhr.send(data);</pre>
            <pre style="font-size:18px; user-select: text;" v-if="is_activeLang===1">
import requests

url = "https://api.themoviedb.org/3/movie/%7Bmovie_id%7D"

payload = "{}"
response = requests.request("GET", url, data=payload)

print(response.text)
            </pre>
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
      endPoint: [
        {methods: 'GET', contents: "Get Images"},
        {methods: 'GET', contents: "Get Details"},
        {methods: 'POST', contents: "Rate Monie"},
        {methods: 'DELETE', contents: "Delete Rating"},
        ],
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
      text-align: start;
      height: 350px;
    }
  }
}
// color
.select {
  &-Ep {
    border-left: 4px solid transparent;
    &-act {
      border-left: 4px solid $primary;
    }
  }
  &-Lang {
    border-bottom: 4px solid transparent;
    &-act {
      border-bottom: 4px solid $primary;
      color: $primary
    }
  }
}
</style>
