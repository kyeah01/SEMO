<template>
<div class="detail">
  <div>
    <div class="detail-Header">
      <h2>개발 가이드</h2>
    </div>
  </div>
  <div>
    <GuideWrite/>
  </div>
</div>
</template>

<script>
import GuideWrite from './guideComponents/GuideWrite'

export default {
  name: 'ApiWriteBottom',
  components: {
    GuideWrite,
  }
}
</script>

<style>

</style>
