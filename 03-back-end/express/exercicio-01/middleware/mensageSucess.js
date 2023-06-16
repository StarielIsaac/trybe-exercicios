const mensageSucess = (req, res, next) => {
    res.status(200);
    console.log("OLÁ AMIGO, BEM VINDO <3")
    next();
};

module.exports = mensageSucess;
