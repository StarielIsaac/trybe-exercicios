// exercicio 06
// Crie a função sendMarsTemperature de forma que:
// A função sendMarsTemperature imprima no console o seguinte texto: “A temperatura de Marte é: temperaturaAtual graus celsius” onde, temperaturaAtual é o valor recebido da função getMarsTemperature; e
// A mensagem deve ser impressa no console depois de no máximo 5 segundos.
const messageDelay = () => Math.floor(Math.random() * 5000);
const getMarsTemperature = () => {
  const maxTemperature = 58;
  return Math.floor(Math.random() * maxTemperature);
};

sendMarsTemperature = (temperature, delay) => {
  setTimeout(() => {
    console.log(`A temperatura de Marte é: ${temperature()} graus celsius`);
  }, delay())
}

sendMarsTemperature(getMarsTemperature, messageDelay)
