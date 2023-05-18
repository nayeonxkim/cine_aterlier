<template>
  <div>
    <h1>Personal</h1>
    <nav>
      <router-link to="/personlogin">Login</router-link> |
      <router-link to="/personsignup">SignUp</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>


export default {
  name: 'PersonalView',
  
}
</script>

<style>

</style>