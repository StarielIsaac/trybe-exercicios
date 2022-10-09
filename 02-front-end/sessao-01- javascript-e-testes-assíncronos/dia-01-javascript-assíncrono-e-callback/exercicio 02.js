// Exercício 02
// callbacks-para-fixar-02.js

const userFullName = ({ firstName, lastName }) => console.log(`Olá! Meu nome é ${firstName} ${lastName}`);
const userNationality = ({ firstName, nationality }) => console.log(`${firstName} é ${nationality}`);

const delay = (maxMilliseconds = 5000) => Math.floor(Math.random() * maxMilliseconds);

const getUser = (callback) => {
  setTimeout(() => {
    const user = {
      firstName: 'Ivan',
      lastName: 'Ivanovich',
      nationality: 'Russo',
    };
    callback(user)
    // Dica: use esse `console.log()` abaixo para imprimir o resultado na tela.
  }, delay());
};

getUser(userFullName); // deve imprimir "Olá! Meu nome é Ivan Ivanovich" depois de um certo tempo
getUser(userNationality); // deve imprimir "Ivan é Russo" depois de um certo tempo




