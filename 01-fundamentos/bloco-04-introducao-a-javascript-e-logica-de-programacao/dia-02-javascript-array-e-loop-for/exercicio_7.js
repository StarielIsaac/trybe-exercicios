let numbers = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27];
let n1 = numbers[0]
let n2 = 0

    for(let cont = 0; cont < numbers.length; cont+=1){
     let n3 = numbers[cont]
     if(n3 <= n1){
        n2 = n3
    } 
}

console.log(n2)
