<template>
<v-container fluid>
    <v-row
    align="center"
    justify="space-around"
  >
    <v-icon medium class="ml-0">mdi-arrow-left-circle</v-icon>
    <v-icon medium class="p-0">mdi-arrow-right-circle</v-icon>
    <v-icon medium class="pl-4">mdi-volume-high</v-icon> 
    <v-icon medium class="">mdi-video-box</v-icon> 
    <v-icon medium class="">mdi-file-pdf-box</v-icon> 
    <v-btn color="error" @click="stopAll()">
      Finish
    </v-btn>
    <v-card
        elevation="0"
        style="height:50px;">
        <p class="pt-4" style="font-size:15px">00/00</p>
    </v-card>
    <Stopwatch v-bind:running="timerEnabled"/>
  </v-row>
  <Dialogs v-if="visibleDialog" v-bind:dialog="true"/>
</v-container>
</template>

<script>
import Stopwatch from './Stopwatch.vue'
import Dialogs from './Dialogs.vue'
    export default {
        components: {
            Stopwatch,
            Dialogs
        },
        data() {
            return {
                visibleDialog:false,
                timerEnabled: true,
                timerCount: 0
            }
        },
        methods: {
            showDialog(dialog) {
                console.log(dialog)
                this.visibleDialog=true
            },
            stopAll() {
                
                this.showDialog('stopAll');
                this.timerEnabled=false
            }
        }

    }

</script>