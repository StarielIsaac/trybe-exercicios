//toLowerCase()
let peca = "Rainha"

switch(peca.toLowerCase()){
    case 'Bispo':
    console.log("O bispo se move em uma linha reta diagonalmente")
    break

    case 'Rei':
    console.log("pode mover-se uma casa em qualquer direção")
    break

    case 'peao':
    console.log("Peão se move somente para frente")
    break

    case 'rainha':
    console.log("Ela pode mover-se qualquer número de casas em linha reta - verticalmente, horizontalmente ou diagonalmente")
    break

    case 'cavalo':
    console.log("O cavalo move-se por duas casas horizontalmente ou verticalmente e então uma casa a mais em uma ângulo reto")
    break

    case 'torre':
    console.log("Se move em linha reta horizontalmente e verticalmente")
    break
    
    }



