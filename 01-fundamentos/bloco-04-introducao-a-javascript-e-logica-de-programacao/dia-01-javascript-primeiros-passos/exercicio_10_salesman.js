const custo = 100
const venda = 150

//insira uma porcentagem do imposto
const imposto = 10

//insira a quantidade de itens vendidos
const quant = 1000

const custoTotal = custo + ((imposto * custo) / 100)
const lucroTotal = venda - custoTotal 

if(custo > 0 || venda > 0){
    console.log(lucroTotal * quant)
} else {
    console.log("Erro, os valores precisam ser maiores que 0")
}
