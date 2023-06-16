const express = require("express");
const routerPosts = require('../controllers/controllerPosts');

const app = express();
app.use(express.json())
//rotas
app.use('/produtos', routerPosts)

module.exports = app;