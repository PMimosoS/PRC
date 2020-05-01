import Vue from 'vue'
import VueRouter from 'vue-router'
import Principal from '../views/Principal.vue'
import Atores from '../views/Atores.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Principal',
    component: Principal
  },
  {
    path: '/filmes',
    name: 'Principal',
    component: Principal
  },
  {
    path: '/atores',
    name: 'Atores',
    component: Atores
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
