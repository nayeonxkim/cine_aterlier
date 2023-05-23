<template>
  <div>
    <div class="modal fade" id="exampleModalToggle" aria-hidden="true" aria-labelledby="exampleModalToggleLabel" tabindex="-1">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalToggleLabel">첫 번째 영화 선택하기</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <SelectMovie />
        </div>
        <div class="modal-footer">
          <button @click="searchedList_reset" class="btn btn-primary" data-bs-target="#exampleModalToggle2" data-bs-toggle="modal" data-bs-dismiss="modal">다음으로</button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="exampleModalToggle2" aria-hidden="true" aria-labelledby="exampleModalToggleLabel2" tabindex="-1">
    <div class="modal-dialog modal-lg modal-dialog-centered">``
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalToggleLabel2">두 번째 영화 선택하기</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <SelectMovie />
        </div>
        <div class="modal-footer">
          <button @click="searchedList_reset" class="btn btn-primary" data-bs-target="#exampleModalToggle" data-bs-toggle="modal" data-bs-dismiss="modal">영화 다시 고르기</button>
          <button @click="searchedList_reset" class="btn btn-primary" data-bs-target="#exampleModalToggle3" data-bs-toggle="modal" data-bs-dismiss="modal">다음으로</button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="exampleModalToggle3" aria-hidden="true" aria-labelledby="exampleModalToggleLabel3" tabindex="-1">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalToggleLabel3">화풍 선택하기</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <SelectPainter />
        </div>
        <div class="modal-footer">
          <button @click="searchedList_reset" class="btn btn-primary" data-bs-target="#exampleModalToggle2" data-bs-toggle="modal" data-bs-dismiss="modal">영화 다시 고르기</button>
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
  computed:{
       isLoading(){
      return this.$store.state.isLoading
      }
    },
  methods:{
    searchedList_reset(){
      return this.$store.commit('SEARCHEDLIST_RESET')
    },
    to_karlo() {
      this.$store.commit('IS_LOADING', true)
      this.$store.dispatch('to_karlo')
      .then(() => {
        this.$store.commit('IS_LOADING', false);
      })
      .catch((error) => {
        // 요청이 실패한 경우에 대한 처리를 수행합니다.
        console.error(error);
        this.$store.commit('IS_LOADING', false); // 요청이 실패하더라도 로딩 상태를 false로 설정합니다.
      });
    }
  },
  destroyed(){
    this.searchedList_reset()
  }
}
</script>

<style>
.modal-body{
  padding: 20px;
}

.loading {
  z-index: 2;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: rgba(0, 0, 0, 0.1) 0 0 0 9999px;
}
</style>