<template>
  <div>
    {{commentItem.content}}
    {{commentItem.author}}
    <button v-if="showDelete" @click="deleteComment">X</button>
  </div>
</template>

<script>
import axios from 'axios'
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
    deleteComment(){
      axios
      .delete(`http://127.0.0.1:8000/articles/${this.articleId}/comments/${this.commentItem.id}/delete/`, {
        headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
      })
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.error(err)
      })
    }
  },
  created(){
    this.showDeleteFunction()
  }
}
</script>

<style>

</style>