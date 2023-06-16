const express = require ('express');
const mensageSucess = require ('../middleware/mensageSucess')
const validadeId = require ('../middleware/validadeId')
const routerPosts = express.Router();

routerPosts.get('/', mensageSucess, (req, res) => {
    return res.status(200).json({message: 'Aqui está todos os posts'})
});

routerPosts.get('/:id', mensageSucess, validadeId, (req, res) => {
    const { id } = req.params
    return res.status(200).json({
        item: id,
        message: 'Aqui está todos os posts por id', 
    })
});

routerPosts.post('/', mensageSucess, (req, res) => {
    const { info } = req.body;
    res.status(200).json({
        message: 'Atualizar as coisas',
        informacoes: info
    });
});

routerPosts.put('/', mensageSucess, (req, res) => {
    return res.status(200).json({message: 'Atualizar as coisas'})
});

routerPosts.delete('/', mensageSucess, (req, res) => {
    return res.status(200).json({message: 'Você deletou o post'})
});

module.exports = routerPosts;