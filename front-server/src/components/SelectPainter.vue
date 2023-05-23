<template>
  <div>
    <div>
      <div
        v-for="painter in painters"
        :key="painter.name"
        :id="painter.name"
        @click="selectPainter(painter.name, $event)"
        :class="{ selected: selectedPainter === painter.name }"
      >
        <img :src="painter.imageSrc" alt="">
        <p>{{ painter.name }}</p>
      </div>
    </div>
    <button @click="clearSelection">Clear Selection</button>
  </div>
</template>

<script>
export default {
  name: 'SelectPainter',
  data() {
    return {
      painters: [
        {
          name: 'Vincent Van Gogh',
          imageSrc: '../assets/Vincent Van Gogh.jpg',
        },
        {
          name: 'Edvard Munch',
          imageSrc: '../assets/Edvard_Munch.jpg',
        },
        {
          name: 'Georges Seurat',
          imageSrc: '../assets/Georges Seurat.webp',
        },
        {
          name: 'Renoir',
          imageSrc: '../assets/Renoir.jpg',
        },
        {
          name: 'Katsushika Hokusai',
          imageSrc: '../assets/Katsushika Hokusai.webp',
        },
        {
          name: 'Mondriaan',
          imageSrc: '../assets/Mondriaan.webp',
        },
        {
          name: 'Frida Kahlo',
          imageSrc: '../assets/Frida Kahlo.png',
        },
        {
          name: 'Andy Warhol',
          imageSrc: '../assets/Andy Warhol.jpg',
        },
      ],
      selectedPainter: '',
    };
  },
  methods: {
    selectPainter(painterName) {
      this.selectedPainter = painterName;
      this.$store.commit('SELECT_PAINTER', painterName);
    },
    clearSelection() {
      this.selectedPainter = '';
      this.$store.commit('SELECT_PAINTER', '');
    },
  },
};
</script>

<style>
#painter:hover {
  cursor: pointer;
  border: solid 5px rgb(221, 102, 102);
}

.selected {
  border: solid 5px rgb(221, 102, 102);
}

img:hover {
  opacity: 0.8;
}

img {
  width: 20%;
}
</style>
