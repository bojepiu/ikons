<template>
  <v-layout row justify-center>
    <v-dialog  v-model="dialog"  v-if="dialog" persistent max-width="450" max-height="600" >
      <v-card >
        <v-card-title>
          <videoPlayer :options="playerOptions"/>  
        </v-card-title>
        <v-card-actions class="d-flex justify-end">
          
          <v-btn color="green darken-1"  @click.native="close">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>
<script>
import 'video.js/dist/video-js.css'
import { videoPlayer } from 'vue-video-player'

  export default {
    components: {
      videoPlayer
    },
    data() {
      return {
         
      }
    },
    props: {
      dialog: {
        default: false
      },
      playerOptions: {
        default:{}
      }
    },
    methods: {
      close() {
        var d=!this.dialog
        this.$emit('update:dialog', d)
        
      }
    }
  }

</script>