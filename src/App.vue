<template>
  <v-app> 
    <Header/>   
    <v-main>
      <router-view/>
    </v-main>

  </v-app>
</template>

<script>
import Header from './components/Header.vue'


//import { LazyYoutube } from "vue-lazytube";
export default {
  name: 'App',
  components:{
    Header
  },
  data: () => ({
  }),
};


</script>
<style scoped>

</style>