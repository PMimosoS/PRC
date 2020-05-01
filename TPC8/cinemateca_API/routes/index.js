var express = require('express');
var router = express.Router();
var Filmes = require('../controllers/filmes')
var Atores = require('../controllers/atores')

/* GET home page. */
router.get('/filmes', function (req, res) {
  Filmes.getLista()
    .then(dados => res.jsonp(dados))
    .catch(e => res.status(500).send(`Erro na listagem de filmes: ${e}`))
});

router.get('/linguas/:id', function (req, res) {
  Filmes.getLinguas(req.params.id)
    .then(dados => res.jsonp(dados))
    .catch(e => res.status(500).send(`Erro na listagem das línguas do filme ${req.params.id}: ${e}`))
});

router.get('/atores', function (req, res) {
  Atores.getLista()
    .then(dados => res.jsonp(dados))
    .catch(e => res.status(500).send(`Erro na listagem dos Atores: ${e}`))
});

module.exports = router;
