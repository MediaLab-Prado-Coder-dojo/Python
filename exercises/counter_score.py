#contador

count_score = 0
#esta funcióón checa el marcador
def score():
  print(count_score)

#esta función suma 1 a score
def mas_uno():
  return count_score + 1

#esta función suma N a score
def mas_n(numero):
  return count_score + numero

#esta función resta 1 a score
def menos_uno():
  return count_score -1

#esta función resta N a score
def menos_n(numero):
  return count_score - numero

#esta función suma o resta 1 a count_score
def masmenos_uno(mas=True):
  if mas == True:
    return count_score + 1
  else:
    return count_score - 1

#cómo podemos guardar el valor de score cada vez?

#cómo podemos guardar todos los scores de la partida?
