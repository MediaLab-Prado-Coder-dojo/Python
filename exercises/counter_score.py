#contador

count_score = 0
#esta función checa el marcador

def score():
  print(count_score)numeroentiendo


score()
print(count_score)


#esta función suma 1 a score
def mas_uno():
  global count_score
  count_score += 1
  return score()


#esta función suma N a score
def mas_n(numero):
  global count_score
  count_score += numero
  return score()

#esta función resta 1 a score
def menos_uno():
  global count_score
  count_score -= 1
  return score()

#esta función resta N a score
def menos_n(numero):
  global count_score
  count_score -= numero
  return score()

#esta función suma o resta 1 a count_score
def masmenos_uno(mas=True, numero=1):
  global count_score

  if mas == True:
    count_score += numero
    return score()
  else:
    count_score -= numero
    return score()

#cómo podemos guardar el valor de score cada vez?

#cómo podemos guardar todos los scores de la partida?

import random
import time

area = (80,80)
comida = [0,0]
serp_loc = [0,0]
long = 1
speed = 1
sentido = 

def poner_comida():
  global comida
  x = random.randrange(80)
  y = random.randrange(80)

  comida[0] = x
  comida[1] = y
  print(comida)

def comer():
  global comida
  global long
  global serp_loc

  if comida == serp_loc:
    long += 1
    speed + 1
    poner_comida()
  else:
    pass

def sentido(direccion):
  global serp_loc
  
  if direccion == 'der':
    serp_loc[0] += 1
  elif direccion == 'izq':
    serp_loc[0] -= 1
  elif direccion == 'arr':
    serp_loc[1] += 1
  else direccion == 'abj':
    serp_loc[1] -= 1

def desplazamiento():
  global serp_loc
  return serp_loc