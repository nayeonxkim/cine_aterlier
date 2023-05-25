<template>
  <div>
    <div id="app" class="mt-0" :class="{'opacity-bg':isLoading}" style="background-color: #ffffff; min-height: 76.8vh;">
      <div id="navbar-main" class="navbar">
        <div id="left-nav" class="d-flex justify-content-start">
          <router-link to="/movie" class="custom-cat p-2">MOVIE</router-link> 
          <router-link to="/community" class="custom-cat p-2">COMMUNITY</router-link> 
        </div>

        <div id="right-nav" class="d-flex justify-content-end">
          <router-link to="/home" class="custom-cat p-2">HOME</router-link> 
          <router-link v-if="!isLoggedIn" to="/" class="custom-cat p-2">Login</router-link> 
          <router-link v-else to="/" class="custom-cat p-2">MYPAGE</router-link> 
        </div>
      </div>
      <div class="logo" :style="logoStyle">CINE ATELIER</div>
      <div class="corret-margin"></div>
      <router-view class="mt-5"/>
    </div>
    <SpinnerView />

    <div style="position: relative; min-height: 30vh;">
      <footer class="py-5 mt-auto" style="position: absolute; bottom: 0; width: 100%; background-color: #000; color:#000; text-align: center;">
        <div class="app-footer-text">
          <h6 style="color: #fff;">nayeon  |  meeseeks</h6>
          <h6 style="color: #fff;">sojeong  |  chadireoroonu</h6>
        </div>
      </footer>
    </div>


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
      const fontSize = this.scrollPosition > 0 ? '30px' : '9vw';
      const logoPadding = this.scrollPosition > 0 ? '11px' : '0px';
      const letterSpacing = this.scrollPosition > 0 ? '0px' : '30px';
      return {
        fontSize: fontSize,
        padding: logoPadding,
        letterSpacing:letterSpacing,
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
  },
};
</script>

<style>

@import url('https://fonts.googleapis.com/css2?family=Blinker&family=Noto+Sans+KR:wght@700&display=swap');
#app {
  text-align: center;
  margin-bottom: 10%;
}


.opacity-bg{
  opacity: 50%;
  pointer-events: none;
}

.logo {
  
  font-family: 'Blinker', sans-serif;
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

.app-footer {
  background-color: #000;
  height: 80px;
  display: flex;
  text-align: center;
  justify-content: center;
}

.app-footer-text {
  color: #ffffff;
  padding-top: 1%;
  /* margin-top: 20%; */
}

</style>
