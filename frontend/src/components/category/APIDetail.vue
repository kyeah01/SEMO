<template>
  <div>
    <div v-show="loadSpinner" class="lds-detail">
      <div class="lds-spinner"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    </div>
    <div class="listDetail">
      <fa-icon icon="times" @click="goList"></fa-icon>
      <APIDetailTop/>
    </div>
    <div class="listDetail">
      <APIDetailMiddle/>
    </div>
    <div class="listDetail">
      <APIDetailBottom/>
    </div>
  </div>
</template>

<script>
import APIDetailTop from './APIDetailTop'
import APIDetailMiddle from './APIDetailMiddle'
import APIDetailBottom from './APIDetailBottom'

export default {
  name: 'APIDetail',
  components: {
    APIDetailTop,
    APIDetailMiddle,
    APIDetailBottom
  },
  props: {
    apiId: {
      type: Number,
      required: true
    }
  },
  data: () => {
    return {
      loadSpinner: true
    }
  },
  watch: {
    loadSpinner() {
      if (this.loadSpinner) {
        document.documentElement.style.overflow = 'hidden'
      }
      document.documentElement.style.overflow = 'auto'
    }
  },
  mounted() {
    document.documentElement.style.overflow = 'hidden'
    this.loadData()
  },
  methods: {
    goList() {
      this.$emit('goList')
    },
    loadData() {
      setTimeout(() => {
        this.loadSpinner = false
      }, 1000);
    }
  }
}
</script>

<style>

</style>
