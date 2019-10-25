<template>
  <div class="apiDetail">
    <div class="listDetail-content">
      <div v-show="loadSpinner" class="lds-detail">
        <div class="lds-spinner"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
      </div>
      <div class="listDetail">
        <fa-icon icon="times" @click="goList" style="z-index: 2;"></fa-icon>
        <APIDetailTop/>
      </div>
      <div class="listDetail">
        <APIDetailMiddle/>
      </div>
      <div class="listDetail listDetail-guide">
        <APIDetailBottom/>
      </div>
    </div>
    <div class="listDetail-ad">
      <!-- <div v-for="item in apiRecommend" :key="item">
        <APIListCard/>
      </div> -->
    </div>
  </div>
</template>

<script>
import APIDetailTop from './APIDetailTop'
import APIDetailMiddle from './APIDetailMiddle'
import APIDetailBottom from './APIDetailBottom'

import APIListCard from './APIListCard'

export default {
  name: 'APIDetail',
  components: {
    APIDetailTop,
    APIDetailMiddle,
    APIDetailBottom,
    APIListCard
  },
  props: {
    apiId: {
      type: Number,
      required: true
    }
  },
  data: () => {
    return {
      loadSpinner: true,
      apiRecommend: [1, 2, 3]
    }
  },
  watch: {
    loadSpinner() {
      if (this.loadSpinner) {
        document.body.style.overflowY = 'hidden'
      }
      document.body.style.overflowY = 'auto'
    }
  },
  mounted() {
    document.body.style.overflowX = 'hidden'
    document.body.style.overflowY = 'hidden'
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
