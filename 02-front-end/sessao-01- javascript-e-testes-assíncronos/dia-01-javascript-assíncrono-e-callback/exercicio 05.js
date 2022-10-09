//exercício 05
//Modifique a função getPlanet, de forma que Marte seja impresso assincronamente, após 4 segundos.
const getPlanet = () => {
  setTimeout(() => {
    const mars = {
      name: 'Mars',
      distanceFromSun: {
        value: 227900000,
        measurementUnit: 'kilometers',
      },
    };
    console.log('Returned planet: ', mars);
  }, 4000)
};

getPlanet();

