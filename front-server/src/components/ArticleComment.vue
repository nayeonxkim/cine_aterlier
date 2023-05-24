<template>
  <div class="comment-container ml-2" style="overflow: hidden;">
    <div class="col-10" style="text-align: left; margin: 0% 3%; padding: 0;">
      <span>{{ commentItem.content }}</span>
    </div>
    <div class="col-1" style="text-align: right; margin-left: 1%">
      <button id="red-btn" class="custom-btn" style="padding: 5px 19px;" v-if="true" @click="deleteComment">X</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'ArticleComment',
  props:{
    commentItem:Object,
    articleId:Number
  },
  data(){
    return {
      showDelete:false
    }
  },
  methods:{
    showDeleteFunction(){
      // console.log(this.$store.state.User)
      // console.log(this.commentItem.author)
      if(this.$store.state.User.id === this.commentItem.author){
        this.showDelete = true
      } else {
        this.showDelete = false
      }
    },
    deleteComment() {
      axios
        .delete(
          `${API_URL}/articles/${this.articleId}/comments/${this.commentItem.id}/delete/`,
          {
            headers: {
              Authorization: `Token ${this.$store.state.token}`,
            },
          }
        )
        .then((res) => {
          console.log(res)
          this.$store.dispatch('getArticleDetail', this.articleId)
        })
        .catch((err) => {
          console.error(err)
        })
    },
  },
  created(){
    this.showDeleteFunction()
  }
}
</script>

<style scoped>
#red-btn:hover {
  background-color: #ff4429 !important;
  color: #000000 !important;
}

.comment-container {
  display: flex;
  align-items: center;
}

.custom-btn {
  text-align: center;
  border: #000 solid 3px;
  border-radius: 0;
  padding: 0.5%;
  background-color: transparent;
}

.custom-btn:hover {
  background-color: #000;
  color: #fff;
}
</style>







