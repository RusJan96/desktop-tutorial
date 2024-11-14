# print(' Hello')
# print(' Nothing')
# print(' will work')
# print(' unless you do')



#  Задание 1
# print(' Anyone who \n    stops \n      learning is old')
# print('            stops')
# print(' learning is old')



# Задание 2 
# a : int = int(input('Введите число a: '))
# b : int = int(input('введите число b: '))

# print(' Сумма a и b :', a + b)
# print(' Разница чисел a и b:', a - b)
# print(' Произведение чисел a и b :', a * b)


# Задание 3
# a : int = int(input('Введите число (значение): '))
# b : int = int(input('введите число (процент): '))

# print( a * (b / 100)  )


# Задание 4 
# a : int = int(input('Введите ширину прямоугольника: '))
# b : int= int(input('введите высоту прямоугольника: '))
# print( a * b )

# модуль 1 урок 3 
# Задание 1

# a = str(input(' введите двухзначное число'))

# print( a[0])
# print( a[1])

#   Задание 2
# a : str = str(input(' введите трехзначное число'))

# print(( a[0]))
# print( (a[1]))
# print( (a[2]))
# print(( int(a[0]) + int(a[1]) + int(a[2]) ))

# Задание 3 
# a : str = str(input(' введите первую цифру  число'))
# b : str = str(input(' введите вторую цифру число'))
# c : int = a + b 
# print(c)

# задание 4
# a : int = int(input(' введите темпиратусу по Цельсию'))
# print( a * 1.8000 + 32)


# 11.07!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# задание 2
# a : int = int(input('введите число'))
# if (a % 7) :
#  print(' Number is not multiple 7')
# else :
#  print(' Number is  multiple 7')


# задание 3
# a : int = int(input(' введите первое  число'))
# b : int = int(input(' введите второе число'))
# if (a > b) :
#     print(a)
# else :
#     print(b)    

#     задание 4
# a : int = int(input(' введите первое  число'))
# b : int = int(input(' введите второе число'))
# if (a > b) :
#     print(b)
# else :
#     print(a)    

#     # задание 5
# a : int = int(input(' введите первое  число'))
# b : int = int(input(' введите второе число'))
# c : str = str(input(' введите знак "+" или "-" или "ср.арф" или "*"'))

# if ( c == '+') :
#     print(a + b)
# if c == '-' and a > b:
#     print( a - b )
# if c == '-' and a < b:
#     print( b - a )
# if c == 'ср.арф' :
#     print( (a + b) / 2)
# if c == '*' :
#     print  (a * b)

                

# модуль 2  операторы ветвлений 
# задание 1
# a : int = int(input(' введите секунды'))
# b : str = str(input(' введите в чем отобразить "ч" , "м" , "с" '))
# c : int = int(60 * 60 * 12) 
# if b == 'ч' :
#     print (c - a / 60 / 60) 
# if b == 'м' :
#     print (c - a / 60)
# if b == 'c' :
#     print (c - a )    

# задание 2
# a : int = int(input(' введите диаметр окружности'))
# b : str = str(input(' введите в чем посчитать "S" или "P" '))
# if b == 'S':
#     print( a / 4 * 3.14) 
# if b == 'P': 
#     print( a * 3.14)

# Задание 3
# a : int = int(input(' введите стоимость одной приставки'))
# b : int = int(input(' введите количество приставок'))
# c : int = int(input(' введите процент скидки'))
# d : str = str(input(' введите выбор общая сумма заказа "C" или стоисоть  одной приставки с учетом скидки "E" '))
# if d == 'C' :
#     print(a * b / 100 * c)
# if d == 'E' : 
#     print( a / 100 * c)

# # задание 4
# a : int = int(input(' введите размер файла в гигабайтах'))
# b : int = int(input(' введите скорость интернет-соединения в битах в секунду '))
# d : str = str(input(' введите в чем отобразить "ч" , "м" , "с" '))
# g : int =  int(a * 8589934592)
# if d == 'ч':
#     print( g / b / 60 / 60)
# if d == 'м':
#     print( g / b / 60 )
# if d == 'с':
#     print( g / b )

# # задание 5 
# a : int = int(input(' введите количество часов'))
# if a >= 0 and a > 6 :
#     print('Good Night')
# if a >= 6 and a < 13 :
#     print(' Good Morning') 
# if  a >= 13 and a < 17 :
#     print('Good Day') 
# if a >= 17 and a <= 24 :
#     print('Good Evening')        

 
# 16.07!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# модуль 2. операторы ветвлений часть 3!
# # задание 2!
# a : list = list(input('введите шестизначное число'))
# if len(a) == 6 :
#     b = a[0]
#     c = a[1]
#     a[0] = a[5]
#     a[5] = b
#     a[1] = a[4] 
#     a[4] = c
#     print(a)
# else :
#     print('не верное число ')

#     задание 3
# a : int = int(input('введите номер месяца'))
# if  1 <= a <= 2 or a == 12:
#     print('Winter')
# elif 3 <= a <= 5:
#     print('Spring')
# elif 6 <= a <= 8:
#     print('Summer')
# elif 9 <= a <= 11:
#     print('Autumn')
# else:
#     print(' неверный номер месяца')  

#     модуль 3. циклы часть 1     
#     задание 1 
# a : int = int(input('введите первое число'))
# b : int = int(input('введите второе число'))
# if a > b:
#     for  i in range (b,a,1):
#         c = i;
#         print(c)
    
# elif b > a:
#     for  i in range (a,b,1):
#         c = i;
#         print(c)
# else :
#     print(' ввели не верные числа')   
#     
# Задание 2
# a : int = int(input('введите первое число'))
# b : int = int(input('введите второе число'))
# if a > b:
#     for  i in range (b,a,2):
#         c = i+1;
#         print(c)
    
# elif b > a:
#     for  i in range (a,b,2):
#         c = i+1;
#         print(c)
# else :
#     print(' ввели не верные числа')       

# Задание 3  оно же и задание 5 !!! 
# a : int = int(input('введите первое число'))
# b : int = int(input('введите второе число'))
# if a > b:
#     for  i in range (b,a,2):
#         c = i;
#         print(c)
    
# elif b > a:
#     for  i in range (a,b,2):
#         c = i;
#         print(c)
# else :
#     print(' ввели не верные числа')       

# задание 4
# a : int = int(input('введите первое число'))
# b : int = int(input('введите второе число'))
# if a > b:
#     for  i in range (a,b,-1):
#         c = i;
#         print(c)
    
# elif b > a:
#     for  i in range (b,a,-1):
#         c = i;
#         print(c)
# else :
#     print(' ввели не верные числа')       

# задание 5 - в 3 задании условия подходят к 5!!!!!





# 18.07!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# модуль 3. циклы часть 2.
# Задание 1
# a : int = int(input('введите первое число'))
# b : int = int(input('введите второе число'))
# c = 0
# s : int = 0
# for i in range(a, b):
#     s += i
# print(s)
# c = s/len(range(a,b))
# print(c)

# задание 2
# a : int = int(input('введите число'))
# b : int = 0
# c : int = 1
# for i in range(1, a + 1):
#     c *= i 
# print(c)
 

#  задание 3 
# a : int = int(input('введите число'))
# print ('*' * a)     


# # задание 4 
# a: int = int(input('введите число'))
# b: str = input('введите символ')

# print (b * a)

# модуль 3. циклы. часть 3
# задание 1
# a : int = int(input('введите число'))
# for i in range (1, 11):
#     print(a, '*', i, '=', a*i)
#     print(f'{a} * {i} = {a * i}')

# задание 2 - пропускаем

# задание 3 
# a : int = int(input('введите первую границу'))
# b : int = int(input('введите вторую границу'))
# c: int = int(input('введите число'))
# d = 0
# while  not a < c <b :
#     print('число ввели не верно')
# for i in range (a , b) :
#     d = i 
    
#     # if d == c :
#     #     print(d)
#     if d == c :
#         print(f'!{d}!')
#     else:
#         print(d)
# задание  4 угадай число

# import random
# b : int = random.randint(0 , 500)
# a : int =  -1

# while not a == b:
#     a : int =  int(input('введите число от 1 до 500 : '))

#     if a > b :
#         print(' ваше число больше')
#     elif a < b : 
#         print(' ваше число меньше')
#     else :
#         print (' ваше число равно загаданному числу!')    
#     print(b)    


# 20.08!!!!!!!!!!!!!!!!!!!                                           for letter in text :
#                                                                    if text[i] =='.' :
#                                                                    text[i+2] == text.upper(text[i+2])
# # модуль 4 строки списки часть 2
# text : str = str(input('введите текст'))
# text1 = text.capitalize()
# n_amount = 0
# digits = '0123456789'
# b = ','
# c = 0
# d = '!'
# t= 0
# for i in range(len(text)):
#     if ((text[i] == '.' or text[i] == '!' or text[i] == '?') and i != len(text) -1):
#         if text == text[i+1] == ' ':
#           text = text[:i+2] + text [i+2].upper() + text[i+3:]
#         else :
#             text = text[:i + 1]  + ' ' + text[ i + 1].upper() + text[ i+2:]




# for letter in text:        
#     if letter in digits:
#         n_amount +=1
# print(f' Количество цифр :{n_amount}')       

# for letter in text:
#     if b in ',':
#         c += 1 
#     print(c)

# for d in text:
#    t += 1 
#    print(t)     
#    Доделать!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# text : str = str(input('введите элементы из списка целых чисел'))
# text1 : str = str(input('введите некоторе число'))
# a = 0
# for tex1 in text:
#     a += 1
#     print(a)
      


# 22.08!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # счатсливый билет задача 
# def is_lucky_ticket(ticket_number : int) :
#     sep_number : list[int] = [int(number) for number in list(str(ticket_number))]   
#     left_part = sum(sep_number [:3])
#     right_part = sum(sep_number [3:])

#     return left_part == right_part 

# print(is_lucky_ticket(123123))
# print(is_lucky_ticket(111111))
# print(is_lucky_ticket(123456))
# print(is_lucky_ticket(456456))
# print(is_lucky_ticket(123564))
# print(is_lucky_ticket(123412))
# print(is_lucky_ticket(985765))

# модуль 5 функции. часть 1
# # задание 2!
# a : int = int(input('введите первое число'))
# b : int = int(input('введите второе число'))
# c : int  = 0
# def display(a: int, b: int) :
#  for i in range(a, b):
#   if i % 2 == 1:
#    print(i)

# print(display(a, b))


# задание 3 !!!!!!!!!!!!!!
# line_lenght : int = int(input('введите длинну'))
# direction : int = int(input('введите направление ( 1 или 2 )'))
# symbol : str = str(input('введите символ'))

# def line(line_lenght: int, direction: int, symbol: str):
#     if direction == 1:
#         for i in range(line_lenght):
#             print(symbol)
#     if direction == 2 :
#         print(symbol * line_lenght )
#     else :
#         print('Ввели не правильное направление')


# line(line_lenght, direction, symbol)   


# задание 4!!!!!!!!!!!!!!!!!!!!!!!!!!
# a : int = int(input('введите первое число '))
# b : int = int(input('введите второе число '))
# c : int = int(input('введите третье число '))
# d : int = int(input('введите четвертое число '))

# def max_2(a : int, b : int):
#     if a >= b :
#         return a
#     elif b > a :
#         return b


# def max_4(a: int, b: int, c : int, d : int):
#     f = max_2(a, b)
#     g = max_2(c, d)
#     return max_2(f, g) 
# print(max_4(a, b, c, d))

# задание 5 !!!!!!!!!!!!!!!!!!!!
         

# 27.08!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# задание со степенью!! функция кторая возводит число в степень через рекурсию!!!!!
# def our_pow( number : int, base: int):
#     temp = number
#     for i in range(base):
#         temp *= number
#         return temp
    
# def rec_pow( number : int, base: int):
#     if base == 1 :
#         return number
#     return rec_pow(  number, base - 1) * number

# написать рекурсивную функцию которая считает сумму от a до b !!
# def summary(a :int , b :int):
#     if a == b - 1 : 
#         return a + b
#     return a + summary(a + 1, b)
# print(summary(1 , 3))

# выводит N звезд в ряд !
# n: int = int(input('введите число '))


# def z(n):
#     if n == 1:
#         return '*'
#     return z(n - 1) + '*'
   

# print(z(n))        
#  задани 5!! жесть не понимаю!!!!!
# numbers: list[int] = [random.randint(a:1, b:100) for _ in range(0 , 100)]




# def min_index_parts_sum(arr: list[int], i:int, n : int = 10):
#     if i == len(arr) - 10:
#         return sum(arr [i:])
#     return min(sum(arr[i:i + 10]), min_index_decate_sum(arr, i + 1, n))

# print( min_index_parts_sum(numbers, n =3))

# 29.08!!!!!!!!!!!!!!!!!!!!!!!!!!! 
# кортежи, множества, словари!!!
# кортеж позволяет выводить информацию, но не позволяет ее изменять!!!! b = (1, 2, 3, 4, 5) - в виде таплов!
#  set - {1, 2, 3, 4} он как массив одинаковые числа не добавляет  : 1, 2, 3, 4, 1 будет 1, 2, 3, 4. отдельный элемент не выведет. сет - это множество!
# есть фишки для них a = {1,2,3} b ={ 3,4,5} выведет 5 при прринт а и б фишки - ^, | , &
# переводит в бинарную Систему счистления
# a = {1, 2, 3} 
# b = {3, 4, 5}
# print( a ^ (a ^ b) )

#    .lower() - сравнивает и большие и маленькие буквы

# задание 1 

# a : str = str(input('введите фрукт '))
# b : int = 0
# fruits : tuple[str] = ('Apple', 'Rasberry', 'lime', 'Apple' )
# for i in fruits:
#         if a == i:
#             b += 1
# print(b)    

# объяснял, есть фотки, вроде все понятно! 



# 3.03.2024!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Модуль 5. Файлы. Тема Файлф чсть 2
# f: TextIO = open()

# f = open('input.txt', encoding='utf-8' )
# f.write('hello')


# Задание 1 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# words: list[str] | None = None
# with open('input.txt', encoding='utf-8') as f :
#  words = f.read().split(' ')

#  with open ('ourput.txt', 'w', encoding='utf-8' ) as f:
#   for word in words:
#    if len(word) >= 7:
#     f.write(word + ' ')

# 
#  Задание 2!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# text1 : list[str] | None = None
# with open('input.txt', encoding='utf-8') as f :
#  text1 = f.readlines()

# with open ('ourput.txt', 'w', encoding='utf-8' ) as f:
#     f.writelines(text1)    


# задание 3 

# words : list[str] | None = None
# with open('input.txt', encoding='utf-8') as f :
#  words = f.read()
# with open ('ourput.txt', 'w', encoding='utf-8' ) as f:
#  for word in words:
   
#    f.write(word + ' ') недоделано!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



# задание 5!!!!
# symbol: str = str(input('введите символ  '))
# count = 0
# words : list[str] | None = None
# with open('input.txt', encoding='utf-8') as f :
#  words = f.read().split(' ')
# #  with open ('ourput.txt', 'w', encoding='utf-8' ) as f:
# print(words)
# for word in words:
#  if word[0] == symbol:
#   count += 1

# print(count) Работает!!!

# задание 6 !!!!!!!!!!!!!!!!!!!!!!!
a : str = '*'
text : str | None = None
with open('input.txt', encoding='utf-8') as f :
 text = f.read()

with open ('ourput.txt', 'w', encoding='utf-8' ) as f:
    for c in text: 
        if a == c:
            f.write('&')
        else:
           f.write(c)






# задание 7!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# mas = []
