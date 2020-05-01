<template>
  <div class="Atores">
    <ListaAtores/>
  </div>
</template>

<script>
// @ is an alias to /src
import ListaAtores from '@/components/ListaAtores.vue'

export default {
  name: 'Atores',
  components: {
    ListaAtores
  }
}
</script>
