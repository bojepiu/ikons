<template>
  <v-app> 
    <Header/>   
    <v-main>
      <router-view/>
    </v-main>
    <v-container justify="center">
  <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="red lighten-2"
          dark
          v-bind="attrs"
          v-on="on"
        >
          Video
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          
        </v-card-title>

        <v-card-text>
          <LazyYoutube
        ref="youtubeLazyVideo"
        src="https://www.youtube.com/watch?v=2TGVPj4YVfk"
        max-width="360px"
        aspect-ratio="16:9"
        thumbnail-quality="standard"
    />
 
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="dialog = false"
          >
            I accept
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div> 
    </v-container>
       
  </v-app>
</template>

<script>
import Header from './components/Header.vue'
import { LazyYoutube } from "vue-lazytube";
export default {
  name: 'App',
  components:{
    Header,
    LazyYoutube
  },
  data: () => ({
    youtubelink:"https://www.youtube.com/watch?v=2TGVPj4YVfk"
  }),
};


</script>
<style scoped>

</style>