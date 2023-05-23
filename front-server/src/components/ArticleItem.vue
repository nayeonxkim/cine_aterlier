<template>
  <div>
    <div class="card" @click="$router.push(`/articles/${articleItem.id}`)">
      <img
      :src="getFullImagePath(articleItem.img)"
      class="card-img-top"
      style="width:100%; height:100%;"
      alt="Article Image">
      <div class="overlay">
        <h6 class="card-title">{{ articleItem.title }}</h6>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    articleItem: Object
  },
  computed: {
    articleList() {
      return this.$store.state.articleList
    }
  },
  methods: {
    getFullImagePath(imageUrl) {
      const API_URL = 'http://127.0.0.1:8000'
      return `${API_URL}${imageUrl}`
    }
  }
}
</script>

<style scoped>
.card {
  width: 100%;
  height: 100%;
}

* {box-sizing: border-box}

/* Container needed to position the overlay. Adjust the width as needed */
.container {
  position: relative;
  width: 50%;
  max-width: 300px;
}

/* Make the image to responsive */
.image {
  display: block;
  width: 100%;
  height: auto;
}

/* The overlay effect - lays on top of the container and over the image */
.overlay {
  position: absolute; 
  bottom: 0; 
  background: rgb(0, 0, 0);
  background: rgba(0, 0, 0, 0.8); /* Black see-through */
  color: #f1f1f1; 
  width: 100%;
  transition: .5s ease;
  opacity:0;
  color: white;
  font-size: 20px;
  padding: 20px;
  text-align: center;
}

/* When you mouse over the container, fade in the overlay title */
.container:hover .overlay {
  opacity: 1;
}

</style>
