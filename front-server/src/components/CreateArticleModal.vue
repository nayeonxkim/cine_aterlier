<template>
  <div class="mb-0">
    <div class="modal" tabindex="-1" role="dialog" id="exampleModalToggle">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Create New Article</h5>
            <button type="button" class="btn" data-bs-dismiss="modal">&times;</button>
          </div>
          <form @submit.prevent="submitForm" enctype="multipart/form-data">
            <div class="modal-body">
              <div class="form-group">
                <label for="fileInput">Image</label>
                <input id="fileInput" type="file" ref="fileInput" accept="image/*" required>
              </div>
              <div class="form-group">
                <label for="titleInput">Title</label>
                <input id="titleInput" v-model="title" type="text" class="form-control" placeholder="Title" required>
              </div>
              <div class="form-group">
                <label for="contentInput">Content</label>
                <textarea id="contentInput" v-model="content" type="text" class="form-control" placeholder="Content" required></textarea>
              </div>
            </div>
            <div class="modal-footer">

              <button type="submit" class="custom-btn" data-bs-dismiss="modal" style="padding: 5px 10px;">Create</button>
              <button type="button" class="custom-btn" data-bs-dismiss="modal" style="padding: 5px 10px;">Close</button>
            </div>
          </form>
        </div>
      </div>
    </div>
      <a class="mt-1 mb-1 custom-btn" data-bs-toggle="modal" href="#exampleModalToggle" role="button" style="padding: 5px 10px;">CREATE</a>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CreateArticleModal',
  data() {
    return {
      title: '',
      content: ''
    }
  },
  methods: {
  
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
  },
  created(){
      this.title = ''
      this.content = ''
  }
}
</script>

<style scoped>
.custom-btn {
  font-weight: 700;
  padding-right: 10px;
  padding-left: 10px;
  border: #000 solid 3px;
  border-radius: 0;
  background-color: transparent;
  margin: 0 auto; /* 가운데 정렬을 위한 margin 속성 추가 */
  display: block; /* 가운데 정렬을 위해 block 요소로 변경 */
  text-decoration: none; /* 텍스트의 밑줄 제거 */
}

.custom-btn:hover {
  background-color: #000 !important;
  color: #fff !important;
  text-decoration: none; /* 텍스트의 밑줄 제거 */
}

.modal-body {
  text-align: left;
}

.form-group {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-bottom: 15px;
}

label {
  margin-bottom: 5px;
}

input[type="text"],
textarea {
  width: 100% !important;
  padding: 5px !important;
  border: 2px solid #000 !important;
  border-radius: 0px !important;
  box-shadow: none !important;
}

</style>
