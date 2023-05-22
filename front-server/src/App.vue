<template>
  <div id="app" class="mt-0">
    <div id="navbar-main" class="navbar">
      <div id="left-nav" class="d-flex justify-content-start">
        <router-link to="/home" class="custom-cat p-2">Home</router-link> 
        <router-link to="/movie" class="custom-cat p-2">Movie</router-link> 
        <router-link to="/community" class="custom-cat p-2">Community</router-link> 
      </div>

      <div id="right-nav" class="d-flex justify-content-end">
        <router-link v-if="!isLoggedIn" to="/" class="custom-cat p-2">Login</router-link> 
        <router-link v-else to="/" class="custom-cat p-2">Logout</router-link> 
      </div>
    </div>
    <div class="logo" :style="logoStyle">Top 100 Popular</div>
    <router-view class="mt-5"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      scrollPosition: 0
    };
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLogin;
    },
    logoStyle() {
      const fontSize = this.scrollPosition > 0 ? '30px' : '50px';
      return {
        fontSize: fontSize
      };
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  destroyed() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    handleScroll() {
      this.scrollPosition = window.scrollY;
    }
  }
};
</script>

<style>
#app {
  text-align: center;
  margin-top: 60px;
}

.logo {
  position: sticky;
  top: 0;
  display: flex;
  justify-content: center;
  border-bottom: 2px solid black;
  background-color: #ffffff;
  padding: 20px 0;
  transition: font-size 0.5s;
}

#navbar-main {
  font-family: 'Blinker', sans-serif;
  background-color: #ffffff;
  font-size: 25px;
}

.custom-cat {
  text-decoration: none;
  color: black;
}

.custom-cat:focus,
.custom-cat:hover {
  color: #ff4429 !important;
}

.custom-cat:active {
  font-weight: bold !important;
  color: #ff4429 !important;
}

#left-nav {
  margin-left: 8px;
}

#right-nav {
  margin-right: 8px;
}
</style>
