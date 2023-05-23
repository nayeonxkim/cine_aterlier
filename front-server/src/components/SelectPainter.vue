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
        <img :src="require(`../assets/${painter.imageSrc}`)" alt="ah">
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
          imageSrc: 'Vincent Van Gogh.jpg',
        },
        {
          name: 'Edvard Munch',
          imageSrc: 'Edvard_Munch.jpg',
        },
        {
          name: 'Georges Seurat',
          imageSrc: 'Georges Seurat.webp',
        },
        {
          name: 'Renoir',
          imageSrc: 'Renoir.jpg',
        },
        {
          name: 'Katsushika Hokusai',
          imageSrc: 'Katsushika Hokusai.webp',
        },
        {
          name: 'Mondriaan',
          imageSrc: 'Mondriaan.webp',
        },
        {
          name: 'Frida Kahlo',
          imageSrc: 'Frida Kahlo.png',
        },
        {
          name: 'Andy Warhol',
          imageSrc: 'Andy Warhol.jpg',
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
