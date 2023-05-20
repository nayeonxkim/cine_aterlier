<template>
  <div>
    <button @click="openModal" class="btn btn-secondary">CREATE</button>
    <div class="modal" tabindex="-1" role="dialog" :class="{ 'show': isModalOpen }">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Create New Article</h5>
            <button type="button" class="close" @click="closeModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <form @submit.prevent="submitForm" enctype="multipart/form-data">
            <div class="modal-body">
              <div class="form-group">
                <label for="fileInput">Image:</label>
                <input id="fileInput" type="file" ref="fileInput" accept="image/*" required>
              </div>
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
              <button type="submit" class="btn btn-primary">Create</button>
              <button type="button" class="btn btn-secondary" @click="closeModal">Close</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CreateArticleModal',
  data() {
    return {
      isModalOpen: false,
      title: '',
      content: ''
    }
  },
  methods: {
    openModal() {
      console.log('열림!')
      this.isModalOpen = true
      console.log(this.isModalOpen)
    },
    closeModal() {
      this.isModalOpen = false
    },
    submitForm() {
      const API_URL = 'http://127.0.0.1:8000'
      const formData = new FormData()
      formData.append('img', this.$refs.fileInput.files[0]) // 이미지 파일 추가
      formData.append('title', this.title)
      formData.append('content', this.content)

      // 유저 정보 가져오기
      const user = this.$store.state.User
      if (user) {
        formData.append('author', user.id)
      }

      axios.post(`${API_URL}/articles/create/`, formData, {
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
          'Content-Type': 'multipart/form-data',
        },
      })
      .then(() => {
        console.log(this.Authorization)
        this.$store.dispatch('get_article_list', 1)
        this.closeModal()
        this.title = ''
        this.content = ''
      })
      .catch((error) => {
        console.error(error)
      })
    }
  }
}
</script>
