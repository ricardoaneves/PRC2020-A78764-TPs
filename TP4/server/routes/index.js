var express = require('express');
var router = express.Router();
var axios = require('axios');

var prefixes = `
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX noInferences: <http://www.ontotext.com/explicit>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX : <http://www.semanticweb.org/ricardo/ontologies/2020/1/arquivo-musica-digital#>
  `;

var repository = 'http://localhost:7200/repositories/arquivo-musica-digital?query=';

router.get('/', function(req, res) {

  var query = `
    select ?o ?titulo (count(?p) as ?count) where {
      ?o :titulo ?titulo.
      ?o :éTocadaPor ?i.
      ?i :éDefinidoPor ?p.
    } group by ?o ?titulo order by desc(?count)`;

  var encoded = encodeURIComponent(prefixes + query)

  axios.get(repository + encoded)
    .then(data => {

      //console.log(data);
      var info = data.data.results.bindings.map(obra => {return {id: obra.o.value.split('#')[1], titulo: obra.titulo.value, count: obra.count.value} });
      console.log(JSON.stringify(info));
      res.render('index', { obras: info });

    })
    .catch(error => res.render('error', {error: error}));

});

router.get('/:id', function(req, res) {

  var id = req.params.id;
  var query = `
    select ?o ?titulo ?compositor ?i ?p ?tipo ?voz where {
      :${id} :titulo ?titulo.
      :${id} :compositor ?compositor.
      :${id} :éTocadaPor ?i.
      ?i :éDefinidoPor ?p.
      ?p :tipo ?tipo.
      optional {
        ?p :voz ?voz
      }
    }`;

  var encoded = encodeURIComponent(prefixes + query)

  axios.get(repository + encoded)
    .then(data => {

      //console.log(data);
      var info = data.data.results.bindings.map(obra => {var voz = ( typeof obra.voz === 'undefined' ) ? '' : obra.voz.value;
                                                         return {titulo: obra.titulo.value, compositor: obra.compositor.value, p: obra.p.value.split('#')[1], tipo: obra.tipo.value, voz:voz} });
      console.log(JSON.stringify(info));
      res.render('obra', { obra: info });

    })
    .catch(error => res.render('error', {error: error}));

});

module.exports = router;