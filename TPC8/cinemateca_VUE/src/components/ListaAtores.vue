<template>
  <v-card class="ma-2">
    <v-card-title>Lista dos Atores na BD</v-card-title>
    <v-card-text>
      <v-data-table
        :headers="hatores"
        :items="atores">

          <template v-slot:no-data>
            <v-alert :value="true" color="warning" icon="warning">
              Ainda não foi possível apresentar uma lista dos atores...
            </v-alert>
          </template>

          <v-template v-slot:items="props">
            <tr @click="rowClicked(props.item)">
              <td>{{ props.item.nome }}</td>
              <td>{{ props.item.sexo }}</td>
            </tr>
          </v-template>
      </v-data-table>
    </v-card-text>
  </v-card>
</template>

<script>
import axios from 'axios'
const lhost = require("@/config/global").host;

export default {
  name: 'ListaAtores',

  data: () => ({
    hatores: [
      {text: "Nome", sortable: true, value: 'nome', class: 'subtitle-1'},
      {text: "Sexo", sortable: true, value: 'sexo', class: 'subtitle-1'},
    ],
    atores: []
  }),

  created: async function(){
    try {
      let response = await axios.get(lhost + "/atores");
      this.atores = response.data
    } 
    catch (e) {
      return e;
    }
  },

  methods: {
    rowClicked: function(item){
      alert('Cliquei no filme: ' + JSON.stringify(item))
    }
  }
  
}
</script>
