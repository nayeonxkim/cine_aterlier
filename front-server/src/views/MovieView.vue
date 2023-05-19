<template>
  <div>
    <h1>MovieView입니다</h1>

    <router-view />
    <PageNav />
  </div>
</template>

<script>
import PageNav from '@/components/PageNav.vue'

export default {
  name: 'MovieView',
  components: {
    PageNav
  },
}
</script>

<style>

</style>