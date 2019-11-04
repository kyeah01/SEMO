<template>

<div>
    <div v-show="loadSpinner" class="lds-parmas">
      <div class="lds-spinner"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    </div>
  <div>
    <h2>2. API Test Console</h2>
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
      <tbody>
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
export default {
  name: 'APIGuideParams',
  data: () => {
    return {
      params: [
        { name: 'movie id', required: "required", type: 'Integer', value: 'Default=1', exam: 'v12', description: "", idx: 0},
        { name: 'api_key', required: "required", type: 'String', value: '지점ID(황사관측 지점 ID 코드표 참조)', exam: '110', description: "", default: "Defalut: <<api_key>>" , idx: 1},
        { name: 'language', required: "optional", type: 'String', value: '지점ID(황사관측 지점 ID 코드표 참조)', exam: '110', description: "Pass a ISO 639-1 value to display translated data for the fields that support it.", default:" Default : en-US", idx: 2},
        { name: 'append_to_response', required: "optional", type: 'String', value: '지점ID(황사관측 지점 ID 코드표 참조)', exam: '110', description: "Append requests within the same namespace to the response.", default: "pattern:([/w]+)", idx: 3}
      ],
      loadSpinner : false
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

    }
  }
}
</script>

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

</style>
