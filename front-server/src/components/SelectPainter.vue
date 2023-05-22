<template>
  <div>
    <div>

      <div id="painter" @click="select_painter">
        <img src="../assets/Vincent Van Gogh.jpg" alt="">
        <p>Vincent Van Gogh</p>
      </div>

      <div id="painter" @click="select_painter">
        <img src="../assets/Edvard_Munch.jpg" alt="">
       <p>Edvard Munch</p>
      </div>

      <div id="painter" @click="select_painter">
        <img src="../assets/Georges Seurat.webp" alt="">
        <p>Georges Seurat</p>
      </div>

      <div id="painter" @click="select_painter">
        <img src="../assets/Renoir.jpg" alt="">
        <p>Renoir</p>
      </div>

      <div id="painter" @click="select_painter">
        <img src="../assets/Katsushika Hokusai.webp" alt="">
        <p>Katsushika Hokusai</p>
      </div>
      
      <div id="painter" @click="select_painter">
        <img src="../assets/Mondriaan.webp" alt="">
        <p>Mondriaan</p>
      </div>

      <div id="painter" @click="select_painter">
        <img src="../assets/Frida Kahlo.png" alt="">
        <p>Frida Kahlo</p>
      </div>

      <div id="painter" @click="select_painter">
        <img src="../assets/Andy Warhol.jpg" alt="">
        <p>Andy Warhol</p>
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
#painter:hover {
  cursor: pointer;
  border: solid 5px rgb(221, 102, 102);
}
  
img:hover{
  opacity:0.8;
}

img{
  width: 20%;
}
</style>