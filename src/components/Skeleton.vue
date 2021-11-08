<template>
  <v-sheet
    v-if="true"
    :color="`grey ${theme.isDark ? 'darken-2' : 'lighten-4'}`"
    class="pa-3"
  >
    <v-skeleton-loader
      class="mx-auto"
      max-width="300"
      height="350"
      type="card-heading,image, actions"
    ></v-skeleton-loader>
  </v-sheet>
</template>
<script>
  export default {
    // Vuetify components provide
    // a theme variable that is
    // used to determine dark
    props:{
        isShowed: {
            type: Boolean,
            default: true
        }
    },
    inject: {
      theme: {
        default: { isDark: false },
      },
    },
  }
</script>