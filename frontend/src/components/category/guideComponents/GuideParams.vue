<template>
<div>
  <div>
    <h2>2. Parameters</h2>
  </div>
  <div style="display: flex;">
    <table>
      <thead>
        <tr>
          <th>PARAMETERS</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in params" :key="item.name">
          <th>{{ item.name }} {{ item.required }} </th>
        </tr>
      </tbody>
    </table>
    <table>
      <thead>
        <tr>
          <th>null</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>null</th>
        </tr>
      </tbody>
    </table>
  </div>
</div>
</template>

<script>
export default {
  name: 'APIGuideParams',
  data: () => {
    return {
      params: [
        { name: 'version', required: true, type: 'String', value: 'Default=1', exam: 'v12'},
        { name: 'jijum_id', required: true, type: 'String', value: '지점ID(황사관측 지점 ID 코드표 참조)', exam: '110'}
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
div, table, th, tr {
  border: 1px solid red;
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
</style>
