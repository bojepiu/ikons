<template>
  <v-container>
      <!-- los tamaños seran de acuerdo al tamaño de las sentencias -->
      <v-card elevation="2" width="260" height="340">
            <v-card-title class="justify-center">{{title}}</v-card-title>
            <hr>
            <v-card-text class="justify-center">
                <v-row>
                <v-img
                contain
                max-height="250"
                max-width="170"
                :src="image_url"
                class="ml-8"
                ></v-img>
                </v-row>
                
                <v-row class="d-flex justify-center">
                    <v-btn class="mx-2" fab dark small color="primary">
                         <v-icon dark>mdi-arrow-left-circle</v-icon>
                    </v-btn>
                    <v-btn class="mx-2" fab dark small color="primary">
                         <v-icon dark>mdi-arrow-right-circle</v-icon>
                    </v-btn>
                    
                </v-row>
                
                <br>
                <hr>
                <br>
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
    //add properties
    
    name: 'Contact-Component',
    props: {'title':String},
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