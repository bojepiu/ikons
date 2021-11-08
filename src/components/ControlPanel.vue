<template>
<v-container fluid>
    <v-row
    align="center"
    justify="space-around"
  >
    <v-btn disabled>Previous</v-btn>
    <v-btn color="primary">
      Next
    </v-btn>
    <v-btn color="error" @click="stopAll()">
      Stop
    </v-btn>
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