<template>
  <div id="app" class="mt-0">
    <nav id="navbar-main" class="navbar fixed-top">
      <div id="left-nav" class="d-flex justify-content-start">
        <router-link to="/home" class="custom-cat p-2">Home</router-link> 
        <router-link to="/movie" class="custom-cat p-2">Movie</router-link> 
        <router-link to="/community" class="custom-cat p-2">Community</router-link> 
      </div>

      <div id="right-nav" class="d-flex justify-content-end">
        <router-link v-if="!isLoggedIn" to="/" class="custom-cat p-2">Login</router-link> 
        <router-link v-else to="/" class="custom-cat p-2">Logout</router-link> 
      </div>
    </nav>
    <div class="box">blank</div>
    <router-view class="mt-5"/>
  </div>
</template>

<script>

export default {
  name: 'App',
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLogin
    }
  },
  components: {

  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Blinker:wght@300&display=swap');

#app {
  /* -moz-osx-font-smoothing: grayscale; */
  text-align: center;
  margin-top: 60px;
}


#navbar-main {
  font-family: 'Blinker', sans-serif;
  background-color: #ffffff;
  font-size: 25px;
  border-bottom: 2px solid black;
  
}

.custom-cat{
  text-decoration: none;
  color:black
}

.custom-cat:focus, .custom-cat:hover {
  color: #ff4429 !important;
}

.custom-cat:active {
  font-weight: bold !important;
  color: #ff4429 !important;
}

/* 왼쪽 세 카테고리 */
#left-nav{
  margin-left: 8px;
  text-decoration-line: none;
}

/* 오른쪽 카테고리 */
#right-nav{
  margin-right:8px;
}

/* nav a.router-link-exact-active {
  font-weight: bold;
  color: #ff4429;
  outline: none;
} */

</style>
