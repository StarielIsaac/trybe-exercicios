let numbers = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27];
let n1 = 0


for(let cont = 0; cont < numbers.length; cont+=1){
let n2 = numbers[cont]
  if(n2 > n1){
    n1 = n2
  } 
}

console.log(n1)
