<template>
  <div>
    <h1>Community</h1>
    <nav>
      <router-link to="/articlelist">Article List</router-link> |
      <router-link to="/articledetail">Article Detail</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'CommunityView',
}
</script>

<style>

</style>