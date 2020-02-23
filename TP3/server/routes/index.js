var express = require('express');
var router = express.Router();
var axios = require('axios');

router.get('/', function(req, res,) {

  axios.get('http://localhost:7200/repositories')
    .then(function(data){

      repositories = [];
      data.data.results.bindings.forEach(element => {

        repositories.push(element.id.value);

      });
      res.render('index', {repositories: repositories})
    })
    .catch(error => res.render('error', {error: error}))

});

router.get('/query', function(req, res) {

  var query = req.query.query;
  var x = query.split('?query=');
  var path = x[0] + '?query=';
  var encoded = encodeURIComponent(x[1]);

  axios.get(path + encoded)
    .then(function(data){

      res.jsonp(data.data);

    })
    .catch(error => res.jsonp(error))

});

module.exports = router;