const validadeId = (req, res, next) => {
    const { id } = req.params;
    const verificar = isNaN(id) ? true : false;
    if(!id | id <= 10 | verificar) {
        console.log(verificar);
        return res.status(400).json({mensage: "Invalid, you need send the id"})
    }
    next()
}

module.exports = validadeId;