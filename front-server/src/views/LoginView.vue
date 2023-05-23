<template>
  <div class="container d-flex justify-content-center">
    <div class="login-container">
      <div v-if="isLogin">
        <button @click="logout" class="btn btn-danger">Log Out</button>
      </div>
      <div v-else>
        <form v-if="!isPopupOpen" @submit.prevent="login">
          <h1 class="title">Login Page</h1>
          <div class="form-group">
            <label for="username">Username:</label>
            <input type="text" id="username" v-model="username" class="form-control">
          </div>

          <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" id="password" v-model="password" class="form-control">
          </div>

          <button @click="login" class="custom-btn">Log In</button>
        </form>

        <form v-else @submit.prevent="signUp">
          <h1 class="title">Sign Up Page</h1>
          <div class="form-group">
            <label for="signup-username">Username:</label>
            <input type="text" id="signup-username" v-model="signupUsername" class="form-control">
          </div>

          <div class="form-group">
            <label for="signup-password1">Password:</label>
            <input type="password" id="signup-password1" v-model="signupPassword1" class="form-control">
          </div>

          <div class="form-group">
            <label for="signup-password2">Password Confirmation:</label>
            <input type="password" id="signup-password2" v-model="signupPassword2" class="form-control">
          </div>

          <button @click="signUp" class="custom-btn">Sign Up</button>
        </form>

        <button @click="togglePopup" class="btn custom-btn" v-text="isPopupOpen ? 'Cancel' : 'Sign Up'"></button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
      isPopupOpen: false,
      signupUsername: null,
      signupPassword1: null,
      signupPassword2: null
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)
    },
    togglePopup() {
      this.isPopupOpen = !this.isPopupOpen
    },
    signUp() {
      const username = this.signupUsername
      const password1 = this.signupPassword1
      const password2 = this.signupPassword2

      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload)
    },
    logout() {
      this.$store.dispatch('logout')
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    // username() {
    //   return this.$store.getters.username
    // }
  },
  created() {
    if (this.isLogin) {
      this.username = this.$store.state.username
    }
  }
}
</script>

<style>
.container {
  margin-top: 50px;
}

.login-container {
  background-color: white;
  padding: 20px;
}
/* .btn {
  margin-top: 15px;
  width: 221px;
} */
.title {
  margin-bottom: 15px;
} 

.custom-btn {
  border: #000 solid 3px;
  border-radius: 0;
  background-color: transparent;
  margin: 0.5% 0.5% 0.5% 0.5%;
}

.custom-btn:hover {
  background-color: #000;
  color: #fff;
}
</style>
