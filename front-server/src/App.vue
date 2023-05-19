<template>
  <div id="app" class="mt-0">
    <nav id="navbar-main" class="navbar px-3 mb-3 custom-background fixed-top">
      <ul class="nav nav-pills">
        <li class="nav-item">
          <router-link to="/home">Home</router-link> |
        </li>
        <li class="nav-item">
          <router-link to="/movie">Movie</router-link> |
        </li>
        <li class="nav-item">
          <router-link to="/community">Community</router-link> |
        </li>
        <li class="nav-item">
          <router-link to="/login">Login</router-link> 
        </li>
      </ul>
    </nav>
    <router-view class="mt-5"/>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#navbar-main {
  background-color: #7e2727;
}

nav a {

  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
