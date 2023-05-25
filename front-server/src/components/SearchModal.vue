<template>
  <div>
    <div class="modal fade" id="exampleModalToggle" aria-hidden="true" aria-labelledby="exampleModalToggleLabel" tabindex="-1">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalToggleLabel">영화 검색</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <SelectMovie />
        </div>
        <div class="modal-footer" style="margin-right: 8.5%">
          <button @click="searchedList_reset" class="custom-btn"
          data-bs-target="#exampleModalToggle2" data-bs-toggle="modal"
          data-bs-dismiss="modal" style="padding: 5px 10px;">다음으로</button>
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
        <div class="modal-footer" style="margin-right: 8.5%">
          <button @click="searchedList_reset" class="custom-btn"
          data-bs-target="#exampleModalToggle" data-bs-toggle="modal"
          data-bs-dismiss="modal" style="padding: 5px 10px;">영화 다시 고르기</button>
          <button @click="searchedList_reset" class="custom-btn"
          data-bs-target="#exampleModalToggle3" data-bs-toggle="modal"
          data-bs-dismiss="modal" style="padding: 5px 10px;">다음으로</button>
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
          <button @click="searchedList_reset" class="custom-btn"
          data-bs-target="#exampleModalToggle2" data-bs-toggle="modal"
          data-bs-dismiss="modal" style="padding: 5px 10px;">영화 다시 고르기</button>

          <button @click="to_karlo" type="button" class="custom-btn"
          data-bs-dismiss="modal" style="padding: 5px 10px;">이미지 생성하기</button>
        </div>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col-12 d-flex justify-content-center">
      <a class="custom-btn" data-bs-toggle="modal" href="#exampleModalToggle" role="button" style="margin: 10px; padding: 5px 10px; text-decoration:none;">나만의 영화 이미지 만들기</a>
    </div>
  </div>

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
    to_karlo() {
      this.$store.dispatch('to_karlo')
    }
  },
  destroyed(){
    this.searchedList_reset()
  }
}
</script>

<style scoped>
.loading {
  z-index: 2;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: rgba(0, 0, 0, 0.1) 0 0 0 9999px;
}

.custom-btn {
  border: #000 solid 3px;
  border-radius: 0;
  background-color: transparent;
}

.custom-btn:hover {
  background-color: #000;
  color: #fff;
}
</style>
