#Condicionais
#= atribue um valor: int, bolean, etc.
#== serve pra comparar igualdades (True, False)
#if, else são "padrões", porém, para caso com várias condicionais, usamos if e depois elif, do segundo if em diante

#Desafio: 
#Encontre o maior dos 2 números

primeiro_numero = input("insira o primeiro número: ")
segundo_numero = input("insira o segundo número: ")

if primeiro_numero > segundo_numero:
  print('n1 é maior que o n2')

elif primeiro_numero == segundo_numero:
  print("os números são iguais, insira um novo número")

elif primeiro_numero < segundo_numero:
  print("n1 é menor que o n2")

else :
  print("você digitou valores inválidos, reinicie o programa")
