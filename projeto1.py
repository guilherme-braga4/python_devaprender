#Projeto: Programa que recebe um número e imprime seu fatorial

numero_fatorial = int(input("digite o número aqui:"))

numero_inicial = 1
acrescimo = 1

while numero_inicial <= numero_fatorial: 
  print(numero_inicial)
  numero_inicial = ((numero_inicial + acrescimo) *    numero_fatorial)

