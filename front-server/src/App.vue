<template>
  <div>
    <div id="app" class="mt-0" :class="{'opacity-bg':isLoading}" style="background-color: #ffffff;">
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
      <div class="logo" :style="logoStyle">FFFF FFFFFFF</div>
      <div class="corret-margin"></div>
      <router-view class="mt-5"/>
    </div>
      <SpinnerView />
  </div>
</template>

<script>
import SpinnerView from '@/views/SpinnerView'
export default {
  name: 'App',
  data() {
    return {
      scrollPosition: 0
    };
  },
  components:{
    SpinnerView
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLogin;
    },
    logoStyle() {
      const fontSize = this.scrollPosition > 0 ? '30px' : '13vw';
      const logoPadding = this.scrollPosition > 0 ? '11px' : '0px';
      return {
        fontSize: fontSize,
        padding: logoPadding,
        transition: 'font-size 0.6s'
      };
    },
    isLoading() {
      return this.$store.state.isLoading;
    },
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
    },
  }
};
</script>

<style>

#app {
  text-align: center;
  margin-bottom: 10%;
}

.opacity-bg{
  opacity: 50%;
  pointer-events: none;
}

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
  font-size: 13vw;
  margin-top: -10%;
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
  margin-left: 2.5%;
}

#right-nav {
  margin-right: 2.5%;
  display: block;
}

.corret-margin {
  padding: 3%;
}

</style>
