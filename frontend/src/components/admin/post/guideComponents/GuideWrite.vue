<template>
<div>
  <div>
    <h2>EndPoint</h2>
  </div>
  <div class="Guide-ep-content">
    <!-- 왼쪽 테이블 -->
    <table class="Guide-ep-table">
      <thead>
        <tr>
          <th><h3>ENDPOINT</h3></th>
        </tr>
      </thead>
      <tbody v-if="edit">
        <tr v-for="(item, index) in endPoint" :key="index">
          <th :class="[{ 'select-Ep-act' : is_activeEp === index }, 'select-Ep']" @click="epSelect(index)">
            <h3>
              <span class="btn"
                :class="{'btn--success' : item.methods == 'POST', 'btn--primary' : item.methods == 'GET' , 'btn--danger' : item.methods == 'DELETE', 'btn--warning' : item.methods == 'PUT'  }"
                @click="switchMethods(index)">
                {{ item.methods }}
              </span>
              <br>
              <!-- {{ item.contents }} -->
              <input class="params-ep" type="text" v-model="item.contents" :placeholder="item.ph">
            </h3>
          </th>
        </tr>
        <tr>
          <fa-icon icon="plus" class="btn" style="font-size: 30px; left: 65px;" @click="plusTable(true)"></fa-icon>
        </tr>
      </tbody>
      <!-- default -->
      <tbody v-else>
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
          <th><h3>PARAMETERS</h3></th>
          <th><h3>Description</h3></th>
          <th><h3>Test Console</h3></th>
        </tr>
      </thead>
      <tbody v-if="edit">
        <!-- is_activeEp -->
        <tr v-for="(item, index) in endPoint[is_activeEp].params" :key="index">
          <th style="width: 20%; height: 100px;"><input class="params-name" type="text" :placeholder="item.name_ph" v-model="item.name">
            <br>
            <span class="btn" :class="{'btn--danger' : item.required === 'required', 'btn--tertiary' : item.required === 'optional'}"
              @click="switchBtn('req', index)">
              {{ item.required }}
            </span>
           </th>
          <th style="width: 100%; text-align: start;">
            <span
              :class="{'tyColor-success' : item.type == 'Integer', 'tyColor-primary' : item.type == 'Boolean', 'tyColor-danger' : item.type == 'String'}"
              @click="switchBtn('type', index)">
              {{ item.type }}
            </span>
            <br> <input class="params-text" v-model="item.description" :placeholder="item.description_ph" type="text">
            <br> <input class="params-text" v-model="item.default" :placeholder="item.default_ph" type="text">
            </th>
          <th><input class="params-test" disabled type="text" placeholder="테스트를 위한 공간입니다."></th>
        </tr>
        <tr>
          <fa-icon icon="plus" class="btn" style="font-size: 30px; left: 600px;" @click="plusTable(false)"></fa-icon>
        </tr>
      </tbody>

      <tbody v-else>
        <tr v-for="item in endPoint[is_activeEp].params" :key="item.idx">
          <th style="width: 20%; height: 100px;">{{ item.name }}
            <br>
            <span class="btn" :class="{'btn--danger' : item.required == 'required', 'btn--tertiary' : item.required == 'optional'}"> {{ item.required }} </span>
           </th>
          <th style="width: 100%; text-align: start;"> <span :class="{'tyColor-success' : item.type == 'Integer', 'tyColor-primary' : item.type == 'Boolean', 'tyColor-danger' : item.type == 'String'}">{{ item.type }}</span> <br> {{ item.description }} <br> {{ item.default }}</th>
          <th><input type="text"></th>
        </tr>
      </tbody>
    </table>
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
  name: 'APIGuideWrite',
  data: () => {
    return {
      edit: true,
      // props
      ep: [
        'GET', 'POST', 'DELETE', 'PUT', 'PATCH'
      ],
      endPoint: [
        {
          methods: 'GET',
          contents: "",
          ph: "ENDPOINP",
          methods_index: 0,
          params: [
            {
              name: '',
              name_ph: 'parameter',
              required: "required",
              required_ph: '',
              type: 'String',
              type_ph: '데이터 타입을 입력해주세요.',
              type_index: 0,
              type_options: ['String', 'Integer', 'Boolean'],
              description: "",
              description_ph: '설명을 입력해주세요.',
              default: "",
              default_ph: '초기 값을 입력해주세요.',
            },
          ],
        },
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
      params: [
        {
          name: '',
          name_ph: 'parameter',
          required: "required",
          required_ph: '',
          type: 'String',
          type_ph: '데이터 타입을 입력해주세요.',
          type_index: 0,
          type_options: ['String', 'Integer', 'Boolean'],
          description: "",
          description_ph: '설명을 입력해주세요.',
          default: "",
          default_ph: '초기 값을 입력해주세요.',
        },
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
    },
    switchMethods(id) {
      if ( this.endPoint[id].methods_index + 1 !== this.ep.length ) {
        this.endPoint[id].methods_index += 1
        this.endPoint[id].methods = this.ep[this.endPoint[id].methods_index]
      } else {
        this.endPoint[id].methods_index = 0
        this.endPoint[id].methods = this.ep[0]
      }
    },
    switchBtn(chk, index) {
      // required switch
      if ( chk === 'req' ) {
        if ( this.endPoint[this.is_activeEp].params[index].required === 'required') {
          this.endPoint[this.is_activeEp].params[index].required = 'optional'
        } else {
          this.endPoint[this.is_activeEp].params[index].required = 'required'
        }
      }
      // type switch
      if ( chk === 'type') {
        if ( this.endPoint[this.is_activeEp].params[index].type_index + 1 !== this.endPoint[this.is_activeEp].params[index].type_options.length ) {
          this.endPoint[this.is_activeEp].params[index].type_index += 1
          this.endPoint[this.is_activeEp].params[index].type = this.endPoint[this.is_activeEp].params[index].type_options[this.endPoint[this.is_activeEp].params[index].type_index]
        } else {
          this.endPoint[this.is_activeEp].params[index].type_index = 0
          this.endPoint[this.is_activeEp].params[index].type = this.endPoint[this.is_activeEp].params[index].type_options[0]
        }
      }
    },
    plusTable(bool) {
      if (bool) {
        this.endPoint.push(
          {
            methods: 'GET',
            contents: "",
            ph: "ENDPOINP",
            methods_index: 0,
            params: [
              {
                name: '',
                name_ph: 'parameter',
                required: "required",
                required_ph: '',
                type: 'String',
                type_ph: '데이터 타입을 입력해주세요.',
                type_index: 0,
                type_options: ['String', 'Integer', 'Boolean'],
                description: "",
                description_ph: '설명을 입력해주세요.',
                default: "",
                default_ph: '초기 값을 입력해주세요.',
              },
            ],
          },
        )
      } else {
        this.endPoint[this.is_activeEp].params.push(
          {
              name: '',
              name_ph: 'parameter',
              required: "required",
              required_ph: '',
              type: 'String',
              type_ph: '데이터 타입을 입력해주세요.',
              type_index: 0,
              type_options: ['String', 'Integer', 'Boolean'],
              description: "",
              description_ph: '설명을 입력해주세요.',
              default: "",
              default_ph: '초기 값을 입력해주세요.',
            }
        )
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.tyColor {
  &-success{
    color: $success
  }
  &-danger{
    color: $danger
  }
  &-warning{
    color: $warning
  }
  &-primary{
    color: $primary
  }
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

.params {
  &-ep {
    border: {
      top: 0;
      left: 0;
      right: 0;
    }
    padding: {
      left: 8px;
    }
    line-height: 25px;
    font-size: 16px;
    width: 160px;
  }
}

.params {
  &-name {
    font-size: 18px;
    width: 90px;
    height: 22px;
    padding: {
      top: 0;
      bottom: 0;
    }
    border: {
      top: 0;
      right: 0;
      left: 0;
    }
  }
  &-text {
    font-size: 16px;
    height: 22px;
    padding: {
      top: 0;
      bottom: 0;
    }
    border: {
      top: 0;
      right: 0;
      left: 0;
    }
    width: 75%;
  }
  &-test {
    font-size: 16px;
    height: 22px;
    padding: {
      top: 0;
      bottom: 0;
    }
    border: {
      top: 0;
      right: 0;
      left: 0;
    }
  }
}
</style>
