## Introdução ao Python

## Parte 0 - Hello, world!
# print("Hello, Python!")

## Parte 1 - Variáveis e tipos de dados
# a = 5
# b = 6.7
# c = "Oi, sou um texto"
# boolean = True # False
# nulo = None

## Parte 2 - Coleções - Lista
# lista_ruim = [1, "oir", None, True, ["as"]]
# lista = [4, 5, 7, 8, 110]

# tamanho = len(lista)
# elemento = lista[3]

# lista.append(99)

# print(tamanho)
# print(elemento)

## Parte 3 - Coleções - Dicionários / hash
# dicionario = {"a": 1, "b": 2, "c": 1}
# dicionario["d"] = 99

# print(dicionario["d"])

## Parte 4 - Estrutura de controle - if
# idade = 29
# if idade >= 60:
#     print("idoso")
# elif idade >= 18:
#     print("adulto")
# else:
#     print("jovem")

## Parte 5 - Estrutura de controle - while
# i = 0
# while i < 10:
#     print(i)
#     i += 1

## Parte 5 - Estrutura de controle - for
# lista
# lista = [4, 5, 7, 8, 110]
# for item in lista:
#     print(item + 10)

# Dicionários
# dicionario = {"a": 1, "b": 2, "c": 1}
# for chave, valor in dicionario.items():
#     print(chave + " - " + str(valor))

## Parte 6 - Funções
# def fahrenheit_para_celsius(temp_fahr):
#     return (temp_fahr - 32) * 5 / 9

# temp_celsius = fahrenheit_para_celsius(70)
# print(temp_celsius)

## Parte 7 - Objetos
# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome

#     def setaIdade(self, idade):
#         self.idade = idade
    
#     def getIdade(self):
#         return self.idade
    
#     def __str__(self):
#         return "Nome: " + self.nome + ", idade: " + str(self.idade)
    
# p = Pessoa("Joao")
# p.setaIdade(30)
# print(p)

## Parte 8 - Ler e escrever em arquivos
# arquivo = open("arquivo.txt", "w")
# arquivo.write("Primeira linha")
# arquivo.close()

# outro = open("arquivo.txt", "r")
# print(outro.read())
# outro.close()

## Pate 9 - Módulos
# import conversor
# c = conversor.fahrenheit_para_celsius(90)
# print(c)

# from conversor import fahrenheit_para_celsius
# c = fahrenheit_para_celsius(88)
# print(c)

entrada = input("Qual o valor?\n")
print(entrada)