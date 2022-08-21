let numbers = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27];
let result = 0
let quant = numbers.length

for(let cont = 0; cont < numbers.length; cont+=1){
    result = numbers[cont] + result
}

console.log("A média aritmética dos valores é: " + (result / quant))