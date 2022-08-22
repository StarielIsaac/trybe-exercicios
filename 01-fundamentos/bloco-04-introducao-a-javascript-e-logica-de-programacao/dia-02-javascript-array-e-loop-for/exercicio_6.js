let numbers = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27];
let n1 = 0
impar = 0


for(let cont = 0; cont < numbers.length; cont+=1){
    if(numbers[cont] % 2 !== 0){
        impar+=1
    }
}

if(impar > 0){
    console.log("Existem " + impar + " números ímpares")
} else if (impar <= 0) {
    console.log("Nenhum valor ímpar encontrado")
}