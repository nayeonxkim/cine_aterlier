<template>
  <div>
    <button @click="openModal">CREATE</button>
    <div v-if="isModalOpen" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <h2>Create New Article</h2>
        <form @submit.prevent="submitForm" enctype="multipart/form-data">
          <input type="file" ref="fileInput" accept="image/*" required />
          <input v-model="title" type="text" placeholder="Title" required />
          <textarea v-model="content" placeholder="Content" required></textarea>
          <button type="submit">Create</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
// CreateArticleModal 컴포넌트
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
      console.log('모달열림')
      this.isModalOpen = true
    },
    closeModal() {
      this.isModalOpen = false
    },
    submitForm() {
      const formData = new FormData()
      const file = this.$refs.fileInput.files[0]
      formData.append('img', file)
      formData.append('title', this.title)
      formData.append('content', this.content)

      this.$store
        .dispatch('create_article', formData)
        .then(() => {
          this.closeModal()
          this.$emit('refresh-articles')
        })
        .catch(error => {
          console.error(error)
        })
    }
  }
}

</script>

<style>

</style>
