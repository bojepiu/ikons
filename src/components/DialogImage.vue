<template>
  <v-layout row justify-center>
    <v-dialog v-model="dialog" persistent max-width="290" >
      <v-card>
        <v-img
        max-height="250" max-width="250"
        contain
        class="pa-4 ml-4"
        v-bind:src="image_url">
        </v-img>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1"  @click.native="close">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>
<script>
  export default {
    data() {
      return {
        
      }
    },
    props: {
      dialog: {
        default: false
      },
      image_url: {
        default: "/404notfoundimage.png"
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