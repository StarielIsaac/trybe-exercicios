const uppercase = (str, callback) => {
      setTimeout(() => {
        callback(str);
      }, 1000);
    };
    
    const upper = (palavra) => {
      console.log(palavra.toUpperCase())
    }
    
    uppercase('one Piece', upper)
    