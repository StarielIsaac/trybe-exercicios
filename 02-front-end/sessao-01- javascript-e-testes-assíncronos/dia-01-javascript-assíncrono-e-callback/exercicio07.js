//exercicio 07
const messageDelay = () => Math.floor(Math.random() * 5000);

//temperatura de Celsius
const getMarsTemperature = () => {
  const maxTemperature = 58;
  return Math.floor(Math.random() * maxTemperature);
};
//transforma para Fahrenheit
const toFahrenheit = (degreeCelsius) => (degreeCelsius * (9 / 5)) + 32;

//mostra mensagem 
const temperatureInFahrenheit = (temperature) =>
  console.log(`Atualmente está ${toFahrenheit(temperature)}ºF em Marte`);

//monstra mensagem 
const greet = (temperature) =>
  console.log(`Olá! Curiosity aqui. Nesse momento está ${temperature}ºC em Marte`);


const sendMarsTemperature = (callback) => {
  const time = messageDelay()
  const temp = getMarsTemperature()
  setTimeout(() => {
    return callback(temp);
  }, time);
}; 

// Imprime "Atualmente está 46.4ºF em Marte", por exemplo
//sendMarsTemperature(temperatureInFahrenheit)

sendMarsTemperature(greet); 
// Imprime "Olá! Curiosity aqui. Nesse momento são 36ºC em Marte", por exemplo
