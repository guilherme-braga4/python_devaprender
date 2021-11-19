#Projeto: Programa que recebe um número e imprime seu fatorial

#entrada
numero_fatorial = int(input("digite o número aqui:"))

#variáveis
resultado = 0
acrescimo = 2

#calculando até 2 operações 
'''
#quando numero_fatorial = acrescimo, o laço para de rodar
while acrescimo < numero_fatorial :
  resultado += numero_fatorial * (numero_fatorial - 1)
  acrescimo += 1
print(resultado)
'''

#calculando corretamente, porém, está executando até a penúltima operação, e , os 0,1 e 2 estavam dando errado!
'''
while acrescimo < 3 :
  resultado += numero_fatorial * (numero_fatorial - 1)
  acrescimo += 1
  numero_fatorial -= 2
  resultado = resultado * numero_fatorial
  #até aqui o máximo de calculo possível, são 2 operações multiplicativas 
if acrescimo == 3:
  while acrescimo < numero_fatorial:
    numero_fatorial -= 1
    resultado = resultado * numero_fatorial
print(resultado)
'''

#calculando perfeitamente

if numero_fatorial == 1 or numero_fatorial == 0:
    print("1")
elif numero_fatorial < 0:
    print("insira um número inteiro")

else:
  while acrescimo < 3 :
    if numero_fatorial == 2:
      resultado += numero_fatorial * (numero_fatorial - 1)
      acrescimo += 1
      print(resultado)
    else:
      resultado += numero_fatorial * (numero_fatorial - 1)
      acrescimo += 1
      numero_fatorial -= 2
      resultado = resultado * numero_fatorial
    #até aqui o máximo de calculo possível, são 2 operações multiplicativas 
  if acrescimo == 3:
    while acrescimo <= numero_fatorial:
      numero_fatorial -= 1
      resultado = resultado * numero_fatorial
  print(resultado)
