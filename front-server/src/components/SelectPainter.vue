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
    <input id="search-input" @keyup.enter="selectCustomPainter" type="text" placeholder="그 외 입력 후 엔터">
    <h3 class="mt-3">{{selectedPainter}}</h3>
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
          imageSrc: 'Egon Schiele.jpg',
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
          imageSrc: 'Katsushika Hokusai.jpg',
        },
        {
          name: 'Mondriaan',
          imageSrc: 'Mondriaan.jpg',
        },
        {
          name: 'Frida Kahlo',
          imageSrc: 'Frida Kahlo.jpg',
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
    selectCustomPainter(event){
      const painterInput = event.target.value
      if(/^[a-zA-Z0-9]+$/.test(painterInput)){
        this.selectedPainter = painterInput
        this.$store.commit('SELECT_PAINTER', this.selectedPainter);
      } else{
        alert('영어와 숫자만 입력가능합니다.')
      }
        event.target.value = ''
    }
  },
};
</script>

<style scoped>
#search-input {
  margin-right: 20px;
  border: solid 3px black;
  padding-left: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
}

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
