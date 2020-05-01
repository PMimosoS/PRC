<template>
  <div class="Principal">
    <ListaFilmes/>
  </div>
</template>

<script>
// @ is an alias to /src
import ListaFilmes from '@/components/ListaFilmes.vue'

export default {
  name: 'Principal',
  components: {
    ListaFilmes
  }
}
</script>
