let array = ['java', 'javascript', 'python', 'html', 'css'];
let maior = array[0]
let menor = array[0]

for(let index = 0; index < array.length; index+=1){
   if(maior.length < array[index].length) {
    maior = array[index]
   } if (menor.length > array[index].length) {
    menor = array[index]    
   }  
}


 console.log(maior)
 console.log(menor)