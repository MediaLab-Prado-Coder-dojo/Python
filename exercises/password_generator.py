import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?+'

print('/'*30)

answer = input('Hola!, ¿Quieres un password más seguro? Escribe s ó n: ')

print('/'*30)

answer_2 = int(input('¿Cuántas contraseñas quieres? '))
lista = []

for l in range(answer_2):
  lista_input = int(input('¿Qué tan larga quieres tu contraseña? Escribe el número: '))
  lista.append(lista_input)


print('/'*30)

print('longitudes: ', lista)

for d in range(answer_2):
  print('/'*30)
  print('contraseña #: ', d+1)
  # print(d)
  password = ''

  if answer == 's':

    long = lista[d]

    for c in range(long):
      choice = random.choice(chars)
      # print(choice)
      password += choice

    print(password)
  
    print('longitud: ', password.__len__())

  else:
    message = 'ok bye bye'
    print(message)
