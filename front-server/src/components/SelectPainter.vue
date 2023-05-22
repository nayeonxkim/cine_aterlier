<template>
  <div>
    <div>
      <div @click="select_painter">
        <p>Pointillism</p>
      </div>

      <div @click="select_painter">
      <p>Vincent Van Gogh</p>
      </div>

      <div @click="select_painter">
      <p>Mondriaan</p>
      </div>

      <div @click="select_painter">
      <p>Edvard Munch</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:'SelectPainter',
  methods:{
    select_painter(event){
      return this.$store.commit('SELECT_PAINTER', event.target.innerText)
    }
  }
}
</script>

<style>

</style>