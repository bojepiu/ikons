import Vue from 'vue'
import VueRouter from 'vue-router'

import Login from '../views/Login.vue'
import Topics from '../views/Topics.vue'
import Cards from '../views/Cards.vue'
import Modules from '../views/Modules.vue'
import Sessions from '../views/Sessions.vue'
import Sentences from '../views/Sentences.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/topics',
    name: 'Topics',
    component:Topics
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
  },
  {
    path: '/cards',
    name: 'Cards',
    component:Cards
  },
  {
    path: '/modules',
    name: 'Modules',
    component:Modules
  },
  {
    path: '/sessions',
    name: 'Sessions',
    component:Sessions
  },
  {
    path: '/sentences',
    name: 'Sentences',
    component:Sentences
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
