//alert(' как дела?')// функция в которую передается строка, и дальше появляется всплывающее уведомление с текстом

// Number ( число) - 10, 3.14
// String (строка) -'JavaScript', 'Phython', "Hello", 'Kill',
// Bool (Булиевый тип) - true/ false

// prompt() -> запрашивает ввод данных
// console.log() -> функция вывод в консоль переданный аргумент

//условия 
// операторы сравнения ==,===, !=, >,<, >=, <=

// ПИШЕМ ПРОГРАММУ КОТОРАЯ ВЫЯСНЯЕТ ЧИЛО ЧЕТНОЕ ИЛИ НЕТ
// typeof() - функция возвращает тип объекта
/*let number = prompt(' Введите число ?:')

if (number % 2 === 0) {
alert ('число четное')
} else {
    alert ('число не четное')
}
*/
 /*let one = prompt('введите возраст ')
 if (one >= 18){
    alert('можно получить права на вождение')
 } else {
    alert (' права на возжение получить нельзя!')
 }
*/
/*let a = prompt('Введите оценку')
a=Number(a)
if  (a>5){
    alert (' оценка не должна превышать 5 баллов!')
}
else if (a===5){
    alert (' отлично')
} else  if (a===4){
    alert ('хорошо')
} else if (a===3){
    alert('удовлетворительно')
} else if (a===2){
    alert (' не удовлетворительно')
} else if (a===1) {
    alert (' ваша оценка кол!!!!')
} else {

} alert(' не верно ввели оценку')
*/
/*
let users =["Nikita", "Stas", "Dysha"]
let gena = "Gena"
users.push(gena)
gena="Kirill"
//alert(users)
// Реализация через While
/* 
let count =0
while ( count != users.lenght){
    alert(users[count])
    count =+1
} 
for(let index =0; index != users.length; index++){
    if (users[index] === 'Stas'){
        users[index] = 'Masha';
    }}
alert(users)
*/
let tasks=[]
let power= true
let command= ''

while ( power === true) {
    alert (' введтите номер команды: 1 -Добавить задачу, 2- Удалить/Закрыть задачу, 3- Выйти из програмы')
comand= Number(prompt )
}