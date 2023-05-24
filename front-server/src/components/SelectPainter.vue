<template>
  <div>
    <div class="row justify-content-center align-items-center">
      <div
        v-for="painter in painters"
        :key="painter.name"
        :id="painter.name"
        @click="selectPainter(painter.name, $event)"
        :class="{ selected: selectedPainter === painter.name }"
        class="col-3"
      >
        <img id="painter-img" :src="require(`../assets/${painter.imageSrc}`)" alt="" >
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
          name: 'Egon Schiele',
          imageSrc: 'Egon Schiele.png',
        },
        {
          name: 'Pablo Picasso',
          imageSrc: 'Pablo Picasso.jpg',
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

<style scoped>
#painter:hover,
.selected {
  cursor: pointer;
  border: solid 3px #000;
}


img:hover {
  opacity: 0.8;
}

img {
  width: 100%;
}
</style>
