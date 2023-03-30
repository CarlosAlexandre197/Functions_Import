#Função 00

def apresentacao(nome, idade, sexo):
    print(f'Olá, {nome}! \nSua idade é: {idade}. \nSexo: {sexo}.')

#Função 01

def soma_dois_numeros(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

#Função 02

def potencia(x, expoente=2):
    return x ** expoente

#Função 03

def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

#Função 04

def mistura_palavras(*args):
    return '_'.join(args)

#Função 05

def descrição_livro(titulo, autor = 'Desconhecido'):
    print(f'Livro: {titulo}. / Autor: {autor}.')
    
#Função 06

def par_impar(numero):
  if numero % 2 == 0:
    return "Par"
  else:
    return "Impar"

#Função 07

def mostra_ate_zero(numero):
  while numero >= 0:
     print(numero)
      numero -= 1
    
#Função 08

def soma_3_numeros(a, b, c):
  return a + b + c

#Função 09 

def positivo_negativo_zero(numero):
  if numero == 0:
    return "Zero"
  elif numero > 0:
    return "Positivo"
  else:
    return "Negativo"

#Função 10

def gorjeta(valor, porcentagem):
  return valor * porcentagem / 100

#Função 11

def conta_letras(letra_buscada, palavra):
  contagem = 0 
  for letra_atual in palavra:
    if letra_atual == letra_buscada:
      contagem += 1
  return contagem
