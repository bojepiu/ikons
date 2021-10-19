import Vue from 'vue'
//import LazyYoutube from "vue-lazytube";
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'


Vue.config.productionTip = false
//Vue.component("LazyYoutube", LazyYoutube);

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')

