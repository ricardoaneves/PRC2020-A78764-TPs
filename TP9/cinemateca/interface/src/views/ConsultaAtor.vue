<template>
  <ConsultaActor :id="$route.params.id"/>
</template>

<script>
// @ is an alias to /src
import ConsultaActor from '@/components/ConsultaAtor.vue'
export default {
  name: 'Consulta',
  components: {
    ConsultaActor
  }
}
</script>