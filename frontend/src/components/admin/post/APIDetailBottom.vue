<template>
<div class="detail">
  <div>
    <div class="detail-Header">
      <h2>개발 가이드</h2>
    </div>
  </div>
  <div>
    <GuideParams/>
    <GuideRes/>
  </div>
</div>
</template>

<script>
import GuideParams from './guideComponents/GuideParams'
import GuideRes from './guideComponents/GuideRes'

export default {
  name: 'ApiWriteBottom',
  components: {
    GuideParams,
    GuideRes
  }
}
</script>

<style>

</style>
