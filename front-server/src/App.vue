<template>
  <div id="app" class="mt-0">
    <div class="backcolor"></div>
    <div id="navbar-main" class="navbar">
      <div id="left-nav" class="d-flex justify-content-start">
        <router-link to="/movie" class="custom-cat p-2">Movie</router-link> 
        <router-link to="/community" class="custom-cat p-2">Community</router-link> 
      </div>
      <div id="right-nav" class="d-flex justify-content-end">
        <router-link to="/home" class="custom-cat p-2">Home</router-link> 
        <router-link v-if="!isLoggedIn" to="/" class="custom-cat p-2">Login</router-link> 
        <router-link v-else to="/" class="custom-cat p-2">Logout</router-link> 
      </div>
    </div>
    <div class="logo" :style="logoStyle">OUR LOGOS</div>
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
      const fontSize = this.scrollPosition > 0 ? '30px' : '110px';
      const logoPadding = this.scrollPosition > 0 ? '11px' : '0px';
      return {
        fontSize: fontSize,
        padding: logoPadding,
        transition: 'font-size 0.5s'
      };
    }
  },
  mounted() {
    this.scrollPosition = window.scrollY;
    window.addEventListener('scroll', this.handleScroll);
    this.handleScroll();
  },
  destroyed() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    handleScroll() {
      this.scrollPosition = window.scrollY;
      // console.log(this.scrollPosition)
    }
  }
};
</script>

<style>
  /* .mt-0 {
    text-align: center;
    margin-top: 60px;
    position: relative;
    display: block;
    max-height: 100vh;
    overflow-y: auto;
    top: 0;
  } */

.logo {
  position: sticky;
  top: 0;
  display: flex;
  justify-content: center;
  border-bottom: 2px solid black;
  background-color: #ffffff;
  padding: 0;
  transition: font-size 0.5s;
  z-index: 990;
  font-size: 80px;
  margin: 0;
}

.backcolor {
  width: 100%;
  background-color: #ffffff;
}

.navbar {
  position: sticky;
  top: 0;
  left: 0;
  width: 100%;
  padding: 0;
  margin: 0;
  z-index: 999;
  background-color: none;
  /* background-color: #ffffff; */
} */


.navbar-content {
  display: flex;
  justify-content: space-between;
  padding: 8px;
  margin: 0;
}


#navbar-main {
  position: sticky;
  font-family: 'Blinker', sans-serif;
  background-color: none;
  font-size: 25px;
  z-index: 999;
}

.custom-cat {
  text-decoration: none;
  color: #000;
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
  display: block;
  margin-left: 8px;
}

#right-nav {
  margin-right: 8px;
  display: block;
}
</style>
