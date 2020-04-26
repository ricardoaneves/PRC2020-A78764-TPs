<template>
    <div v-if="!this.loaded">
        Loading...
    </div>
    <v-card class="ma-4" v-else>
        <v-card-title class="indigo darken-4 white--text" dark>
            <span class="headline">Filme: "{{ filme.info.titulo }}" ({{id}})</span>
        </v-card-title>

        <v-card-text>
            <v-container>
            <v-row>
                <v-col cols="2">
                <div class="info-label">Resumo</div>
                </v-col>
                <v-col>
                <div class="info-content">{{ filme.info.res }}</div>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="2">
                <div class="info-label">Data</div>
                </v-col>
                <v-col>
                <div class="info-content">{{ filme.info.data }}</div>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="2">
                <div class="info-label">Língua</div>
                </v-col>
                <v-col>
                <div class="info-content">{{ filme.info.lingua }}</div>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="2">
                <div class="info-label">Duração (minutos)</div>
                </v-col>
                <v-col>
                <div class="info-content">{{ filme.info.duracao }}</div>
                </v-col>
            </v-row>

            <v-row>
                <v-col cols="2">
                <div class="info-label">Índice de Popularidade</div>
                </v-col>
                <v-col>
                <div class="info-content">{{ filme.info.pop }}</div>
                </v-col>
            </v-row>
            </v-container>
        </v-card-text>

        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="$router.go(-1)"> - Voltar</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
import axios from 'axios'
const lhost = require("@/config/global").host;
export default {
  name: 'Consulta Filme',
  props: ['id'], 
  data: () => ({
    footer_props: {
      "items-per-page-text": "Mostrar",
      "items-per-page-options": [10, 20, 50, 100, -1],
      "items-per-page-all-text": "Todos"
    }, 
  filme: {},
  loaded: false
  }),
  created: async function(){
    try {
      let response = await axios.get(lhost + "/filmes/" + this.id);
      this.filme = response.data
      this.loaded = true;
    } 
    catch (e) {
      return e;
    }
  },
  methods: {
    
  }
}
</script>