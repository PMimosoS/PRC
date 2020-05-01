var express = require('express')
var router = express.Router()
var axios = require('axios')


// ------------------Tratamento dos pedidos-------
/* GET users listing. */
router.get('/', function(req, res, next) {
  axios.get('http://localhost:4019/api')
        .then(repositorios => res.render('index', {repositorios: repositorios.data}))
        .catch(error =>{
            console.log('Erro: ' + error)
        })
})

module.exports = router;
