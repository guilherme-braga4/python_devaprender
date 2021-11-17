#Projeto 2: gerar valor aleatório entre 1 a 10, e permite que o usuário chute um valor, que enquanto não for igual ao número aleatório, continuará pedindo pra ele tentar noamente
from random import randrange
#randrange é uma biblioteca que gera valores aleatórios



valor_chute = int(input("insira seu valor da sorte: "))
print(randrange(1,10)) 
valor_gerado = randrange

while valor_gerado != valor_chute:
  if valor_chute < valor_gerado:
      print("você chutou pra baixo")
      int(input("digite seu valor novamente"))
  elif valor_chute > valor_gerado:
      print("você chutou pra cima")
      int(input("digite seu valor novamente"))
  else:
      print("parabéns, você acertou")