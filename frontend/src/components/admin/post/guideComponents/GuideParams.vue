<template>

<div>
    <div v-show="loadSpinner" class="lds-parmas">
      <div class="lds-spinner"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    </div>
  <div>
    <h2>API Test Console</h2>
  </div>
  <div style="display: flex;" >
    <table class="Guide-ep-subTable">
      <thead>
        <tr>
          <th>PARAMETERS</th>
          <th>Description</th>
          <th>Test Console</th>
        </tr>
      </thead>
      <tbody v-if="edit">
        <tr v-for="(item, index) in params" :key="index">
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
          <fa-icon icon="plus" class="btn" style="font-size: 30px; left: 600px;" @click="plusTable"></fa-icon>
        </tr>
      </tbody>

      <tbody v-else>
        <tr v-for="item in params" :key="item.idx">
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
  <div style="width:100%;text-align: end;">
    <div class="btn btn--danger btn--lg" @click="axiosSend()">API TEST</div>
  </div>
</div>
</template>

<script>
import Multiselect from 'vue-multiselect'

export default {
  name: 'APIGuideParams',
  components: {
    Multiselect
  },
  props: {
    edit: {
      type: Boolean,
      required: false,
      default: true
    }
  },
  data: () => {
    return {
      // params: [
      //   { name: 'movie id', required: "required", type: 'Integer', value: 'Default=1', exam: 'v12', description: "", idx: 0},
      //   { name: 'api_key', required: "required", type: 'String', value: '지점ID(황사관측 지점 ID 코드표 참조)', exam: '110', description: "", default: "Defalut: <<api_key>>" , idx: 1},
      //   { name: 'language', required: "optional", type: 'String', value: '지점ID(황사관측 지점 ID 코드표 참조)', exam: '110', description: "Pass a ISO 639-1 value to display translated data for the fields that support it.", default:" Default : en-US", idx: 2},
      //   { name: 'append_to_response', required: "optional", type: 'String', value: '지점ID(황사관측 지점 ID 코드표 참조)', exam: '110', description: "Append requests within the same namespace to the response.", default: "pattern:([/w]+)", idx: 3}
      // ],
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
      loadSpinner : false,
    }
  },
  methods: {
    axiosSend() {
      this.loadSpinner = true
      setTimeout(() => {
        this.loadSpinner = false
      }, 1500);
      setTimeout(() => {
        alert("요청 완료하였습니다.")
      }, 1600);
    },
    plusTable() {
      this.params.push(
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
    },
    switchBtn(chk, index) {
      // required switch
      if ( chk === 'req' ) {
        if ( this.params[index].required === 'required') {
          this.params[index].required = 'optional'
        } else {
          this.params[index].required = 'required'
        }
      }
      // type switch
      if ( chk === 'type') {
        if ( this.params[index].type_index + 1 !== this.params[index].type_options.length ) {
          this.params[index].type_index = this.params[index].type_index + 1
          let reIndex = this.params[index].type_index
          this.params[index].type = this.params[index].type_options[reIndex]
        } else {
          this.params[index].type_index = 0
          this.params[index].type = this.params[index].type_options[0]
        }
      }
    }
  }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style lang="scss" scoped>
div, table, th, tr {
  border: 1px solid white;
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

thead tr th {
  font-size: 22px;
}

tbody tr th input {
  padding-left: var(--space-sm);
  font-size: 22px;
  height: 30px;
  width: 200px;
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
