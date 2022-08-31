function createDaysOfTheWeek() {
    const weekDays = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
    const weekDaysList = document.querySelector('.week-days');
  
    for (let index = 0; index < weekDays.length; index += 1) {
      const days = weekDays[index];
      const dayListItem = document.createElement('li');
      dayListItem.innerHTML = days;
  
      weekDaysList.appendChild(dayListItem);
    };
  };
  
  createDaysOfTheWeek();
  
  // Escreva seu código abaixo.

  let decemberDaysList = [29, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31];

//01
  function create() { 
  const days = document.getElementById('days');
  
  for(let i = 0; i < decemberDaysList.length; i += 1){

    const lista = document.createElement('li')
    lista.innerText = decemberDaysList[i];
    lista.className = 'day'
        if(decemberDaysList[i] === 24 || decemberDaysList[i] === 31){
            lista.className = 'day holiday' 
        } if (decemberDaysList[i] === 4 || decemberDaysList[i] === 11 || decemberDaysList[i] === 18) {
            lista.className = 'day friday'
        } else if (decemberDaysList[i] === 25 ) {
            lista.className = 'day friday holiday'
        }

  days.appendChild(lista);
   }
  }
  create()

//02
  function makebutton(param){
    const make = document.createElement('button');
    let newId = 'btn-holiday'
    make.innerHTML = param
    make.id = newId
    const conteiner = document.querySelector('.buttons-container')
    conteiner.appendChild(make)
  }
  makebutton('Feriados')

//03

  function background() {
    const feriado = document.querySelectorAll('.holiday')
    const conteiner = document.getElementById('btn-holiday')
    const color = 'blue'
    const colorBack = 'black'
    conteiner.addEventListener('click', function(){
        for(let i = 0; i < feriado.length; i += 1){
            if(feriado[i].style.backgroundColor === colorBack){
                feriado[i].style.backgroundColor = color
            } else {
                feriado[i].style.backgroundColor = colorBack
            }
        }       
    }) 
  }

  background()


  //04

  function sexta(sextaFeira){
    const conteiner = document.querySelector('.buttons-container')
    const addbotton = document.createElement('button')
    addbotton.id = 'btn-friday'
    addbotton.innerText = sextaFeira
    conteiner.appendChild(addbotton)
  }

sexta('Sexta-feira')


//05 
function modifica (test){
    const conteiner = document.getElementById('btn-friday')
    const sextas = document.querySelectorAll('.friday')
    const text = "Sextou!!"
    conteiner.addEventListener('click', function(){
        for(let index = 0; index < sextas.length; index += 1) {
            if(sextas[index].innerHTML !== text){
                sextas[index].innerHTML = text
            } else { 
                sextas[index].innerHTML = test[index]
            }
        }
    })
}

modifica(['4', '11', '18', '25'])



//06

function mouseEntrou(){
    const mouse = document.querySelector('#days')
    mouse.addEventListener('mouseover', function(event) {
    event.target.style.fontSize = '40px'
    event.target.style.fontWeight = '800'
    })
}

function mouseSaiu(){
    const mouse = document.querySelector('#days')
    mouse.addEventListener('mouseout', function(event) {
    event.target.style.fontSize = '20px'
    event.target.style.fontWeight = '100'
    })    
}

mouseEntrou()
mouseSaiu()


//07

function newTaskSpan(task) {
    let tasksContainer = document.querySelector('.my-tasks');
    let taskName = document.createElement('span');
  
    taskName.innerHTML = task;
    tasksContainer.appendChild(taskName); 
  }

  newTaskSpan('Nova Tarefa:');
 
08 

function newTaskDiv(color) {

    let tasksContainer = document.querySelector('.my-tasks');
    let newTask = document.createElement('div');
  
    newTask.className = 'task';
    newTask.style.backgroundColor = color;
    tasksContainer.appendChild(newTask); // Adiciona newTask como filho de tasksContainer
  }


  newTaskDiv('red');




  //09

  function setTaskClass() {
    let selectedTask = document.getElementsByClassName('task selected');
    let myTasks = document.querySelector('.task');
    myTasks.addEventListener('click', function(event) {
      if (selectedTask.length === 0) {
        event.target.className= 'task selected';
      } else {
        event.target.className = 'task';
      }
    });
  }
  //chamando funcão
  setTaskClass();




  //10

  function setDayColor() {
    let selectedTask = document.getElementsByClassName('task selected');
    let days = document.querySelector('#days');
    let taskDiv = document.querySelector('.task');
    let taskColor = taskDiv.style.backgroundColor;
    
    days.addEventListener('click', function(event){
      let eventTargetColor = event.target.style.color;
      if (selectedTask.length > 0 && eventTargetColor !== taskColor) {
        let color = selectedTask[0].style.backgroundColor; // Pega a cor de fundo do primeiro elemento salvo na variável "selectedTask" e salva na variável "color"
        event.target.style.color = color; // atribui a cor salva na variável "color" ao evento alvo
      } else if (eventTargetColor === taskColor) {
        event.target.style.color = 'rgb(119,119,119)';  // Altera a cor de fundo do evento alvo para "rgb(119, 119, 119)"
      }
    });
  }
   //chamando funcão
  setDayColor();
