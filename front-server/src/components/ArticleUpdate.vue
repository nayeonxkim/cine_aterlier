<template>
  <div>
    <p>{{articleId}}번 게시글 수정페이지</p>
    <form @submit.prevent="submitForm" enctype="multipart/form-data">
      <div class="modal-body">
        <div class="form-group">
          <label for="titleInput">Title:</label>
          <input id="titleInput" v-model="title" type="text" class="form-control" placeholder="Title" required>
        </div>
        <div class="form-group">
          <label for="contentInput">Content:</label>
          <textarea id="contentInput" v-model="content" class="form-control" placeholder="Content" required></textarea>
        </div>
        </div>
        <div class="modal-footer">
          <button type="submit" class="btn btn-primary">Update</button>
          <button type="button" class="btn btn-secondary" @click="closeModal">Close</button>
        </div>
    </form>
  </div>
</template>

<script>
// import axios from 'axios'
export default {
  computed:{
    articleId(){
      return this.$route.params.articleId
    }
  },

  methods:{

    }
  
}
</script>

<style>

</style>