import Vue from 'vue'
import VueRouter from 'vue-router'
import Principal from '../views/Principal.vue'
import Atores from '../views/Atores.vue'
import Consulta from '../views/Consulta.vue'
import ConsultaAtor from '../views/ConsultaAtor.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/filmes',
    name: 'Filmes',
    component: Principal
  },
  {
    path: '/atores',
    name: 'Atores',
    component: Atores
  },
  {
    path: '/filmes/:id',
    name: 'Consulta Filme',
    component: Consulta
  },
  {
    path: '/atores/:id',
    name:'Consulta Ator',
    component: ConsultaAtor
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
