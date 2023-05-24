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
        <div class="modal-footer">
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
        <div class="modal-footer">
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
  <a class="custom-btn" data-bs-toggle="modal" href="#exampleModalToggle" role="button" style="padding: 5px 10px; text-decoration:none;">영화 검색</a>
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
  // computed:{
    //    isLoading(){
    //   return this.$store.state.isLoading
    //   }
    // },
  methods:{
    searchedList_reset(){
      return this.$store.commit('SEARCHEDLIST_RESET')
    },
    to_karlo() {
      // this.$store.commit('IS_LOADING', true)
      this.$store.dispatch('to_karlo')
      .then(() => {
        // this.$store.commit('IS_LOADING', false);
      })
      .catch((error) => {
        // 요청이 실패한 경우에 대한 처리를 수행합니다.
        console.error(error);
        // this.$store.commit('IS_LOADING', false); // 요청이 실패하더라도 로딩 상태를 false로 설정합니다.
      });
    }
  },
  destroyed(){
    this.searchedList_reset()
  }
}
</script>

<style scoped>
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

.custom-btn {
  border: #000 solid 3px;
  border-radius: 0;
  background-color: transparent;
  margin: 0.5% 0.5% 0.5% 0.5%;
  padding: 1% 2%  /* 여기 윈도우, 맥 호환 문제인지 확인 할 것 */
}

.custom-btn:hover {
  background-color: #000;
  color: #fff;
}
</style>
