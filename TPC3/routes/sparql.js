var express = require('express')
var router = express.Router()
var axios = require('axios')


// ------------------Tratamento dos pedidos-------
/* GET users listing. */
router.get('/input', function(req, res, next) {
    axios.get('http://localhost:4019/api')
    .then(repositorios => res.render('getInput', {repositorios: repositorios.data}))
    .catch(error =>{
        console.log('Erro: ' + error)
    })
})

router.post('/input', function(req, res, next){
    var query = req.body.intext
    var botao = req.body.option
    var repositorio = req.body.repositorio
    var encoded = encodeURI(query)
    axios.get('http://localhost:7200/repositories/'+repositorio+'?query='+ encoded, { headers: { "Content-Type": "application/sparql-results"+ botao } })
        .then(response =>{
            //res.setRequestHeader('Content-Type', 'application/sparql-results+json')
            res.jsonp(response.data)
        })
        .catch(error =>{
            console.log('Erro: ' + error)
        })
})

module.exports = router;
