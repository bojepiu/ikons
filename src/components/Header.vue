<template>
<v-app-bar
      app
      color="blue darken-4"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="30"
        />

      </div>
        <v-tabs  slider-color="blue">
            <v-tab to="/">Login</v-tab>
            <v-tab to="modules">Modules</v-tab>
            <v-tab to="sessions">Sessions</v-tab>
            <v-tab to="sentences">Sentences</v-tab>
            <v-tab to="topics">Topics</v-tab>
            <v-tab to="cards">Cards</v-tab>
            <v-tab to="tests">Tests</v-tab>
        </v-tabs>
        
    </v-app-bar>
</template>
<script>
export default {
    name: 'Header'
  }
</script>

<style>

</style>