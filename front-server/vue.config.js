const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

module.exports = {
  devServer: {
    proxy: {
      '/static': {
        target: 'http://127.0.0.1:8000/movies',  // Django 프로젝트의 도메인 주소
        changeOrigin: true
      }
    }
  }
};