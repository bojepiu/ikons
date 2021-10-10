<template>
  <v-container class="justify-center spacing-playground pa-12" fluid>
      <v-row justify="space-around">
      <v-card elevation="4" width="360" height="280">
          <v-card-title class="blue darken-3"><span class="white--text">Ingrese sus credenciales</span></v-card-title>
        <v-form ref="form" v-model="valid" lazy-validation>            
            <v-text-field append-icon="mdi-account" type="text" placeholder="Usuario" autofocus class="justify-center spacing-playground pa-4"></v-text-field>
            <v-text-field append-icon="mdi-lock"  type="password" placeholder="Contraseña" class="justify-center spacing-playground pa-4"></v-text-field>
            <v-row class="d-flex justify-end mb-6">  
                <v-btn depressed color="primary" class="pa-4 mr-6" >Login</v-btn>
            </v-row>
        </v-form>
      </v-card>
      </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'Login'
  }
</script>
