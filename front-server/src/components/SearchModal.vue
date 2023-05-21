<template>
  <div>
    <div class="modal fade" id="exampleModalToggle" aria-hidden="true" aria-labelledby="exampleModalToggleLabel" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalToggleLabel">영화 선택하기</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <SelectMovie />
        </div>
        <div class="modal-footer">
          <button class="btn btn-primary" data-bs-target="#exampleModalToggle2" data-bs-toggle="modal" data-bs-dismiss="modal">다음으로</button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="exampleModalToggle2" aria-hidden="true" aria-labelledby="exampleModalToggleLabel2" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalToggleLabel2">화풍 선택하기</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <SelectPainter />
        </div>
        <div class="modal-footer">
          <button class="btn btn-primary" data-bs-target="#exampleModalToggle" data-bs-toggle="modal" data-bs-dismiss="modal">영화 다시 고르기</button>
          <button @click="to_karlo" type="button" class="btn btn-secondary" data-bs-dismiss="modal">이미지 생성하기</button>
        </div>
      </div>
    </div>
  </div>
  <a class="btn btn-primary" data-bs-toggle="modal" href="#exampleModalToggle" role="button">나만의 포스터 생성하기</a>
  </div>
</template>

<script>
import SelectMovie from '@/components/SelectMovie.vue'
import SelectPainter from '@/components/SelectPainter.vue'
export default {
  name:'SearchModal',
  components:{
    SelectMovie,
    SelectPainter
  },
  methods:{
    searchedList_reset(){
      return this.$store.commit('SEARCHEDLIST_RESET')
    },
    to_karlo(){
      return this.$store.dispatch('to_karlo')
    }
  },
  destroyed(){
    this.searchedList_reset()
  }

}
</script>

<style>

</style>