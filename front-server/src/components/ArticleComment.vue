<template>
  <div>
    {{commentItem.content}}
    {{commentItem.author}}
    <button v-if="true" @click="deleteComment">X</button>
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

<style>

</style>