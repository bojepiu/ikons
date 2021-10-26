<template>
  <v-container>
      <v-card elevation="2" width="200" height="255">
            <v-card-title class="justify-center">{{title}}</v-card-title>
            <v-card-text class="justify-center">
                <v-row>
                <v-img
                contain
                max-height="90"
                max-width="170"
                :src="image_url"
                class="ml-4"
                ></v-img>
                </v-row>
                <v-row>
                    <v-text-field readonly v-model="description"></v-text-field>
                </v-row>
                <v-row class="d-flex justify-center">
                    <v-icon large border @click="play_audio">mdi-volume-high</v-icon> 
                    <v-icon large border>mdi-video-box</v-icon> 
                    <v-icon large border>mdi-file-pdf-box</v-icon> 
                </v-row>
            </v-card-text>
        </v-card>
  </v-container>
</template>

<script>
export default {
    name: 'Contact-Component',
    data(){
        return{
            image_card:null,
            image_url:"404notfoundimage.png",
            track_url:"",
            audio_url:null
        }
    }
}
</script>

<style>

</style>