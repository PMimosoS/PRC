var express = require('express')
var router = express.Router()
var axios = require('axios')


router.get('/', function(req, res, next) {
    axios.get('http://localhost:7200/repositories')
          .then(response =>  {
              res.jsonp(response.data)
          })
          .catch(error =>{
              console.log('Erro: ' + error)
          })
  })
  

module.exports = router;