let array = ['java', 'javascript', 'python', 'html', 'css'];
let maior = array[0]
let menor = array[0]

for(let index = 0; index < array.length; index+=1){
   if(maior < array[index]) {
    maior = array[index]
   } if (menor > array[index]) {
    menor = array[index]    
   }  
}


 console.log(maior)
 console.log(menor)