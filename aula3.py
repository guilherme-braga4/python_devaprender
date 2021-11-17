'''
estrutura de um laço de repetição 
for (nome da constante) in (nome da coleção(x,y)):
coleção -> range: exibe de x até (y-1)
outra opção para range: (x,y,z) sendo Z o intervalo
'''

# a coleção é uma array qualquer: nome_da_array = ['a,b,c']

#Desafio - imprimir um número de 1 a N

N = int(input("digite o valor N:"))
#convertemos N para inteiro, pois ele é recebido como string
I = 1

#se quiser adicionar o valor N também, basta colocar N+1 dentro do range

for intervalo in range(I,N):
  print(intervalo)
 