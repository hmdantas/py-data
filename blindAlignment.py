#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Implementação do algoritmo "Blind Alignment"

Cauteruccio F., Fortino G., Guerrieri A., Terracina G. (2014) Discovery of Hidden Correlations between Heterogeneous Wireless Sensor Data Streams. In: Fortino G., Di Fatta G., Li W., Ochoa S., Cuzzocrea A., Pathan M. (eds) Internet and Distributed Computing Systems. IDCS 2014. Lecture Notes in Computer Science, vol 8729. Springer, Cham

'''


from random import shuffle
from math import factorial

def editdistance(str1, str2):
    '''
    Algoritmo para encontrar a edit distance entre duas strings encontrado em
    https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
    com pequenas alterações
    '''

    m = len(str1)
    n = len(str2)

    # Create a table to store results of subproblems
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
 
    # Fill d[][] in bottom up manner
    for i in range(m+1):
        for j in range(n+1):
 
            # If first string is empty, only option is to
            # isnert all characters of second string
            if i == 0:
                dp[i][j] = j    # Min. operations = j
 
            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i    # Min. operations = i
 
            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
 
            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])    # Replace
 
    return dp[m][n]

def editdistance(str1, str2, M):
    '''
    Função para encontrar o edit distance entre as strings 1 e 2 dado o matching
    schema M.
    '''


def initialize(M):

    '''
    Função para inicializar a matriz booleana representando o matching schema. 
    Escolheu-se arbitrariamente que a matriz M0 é inicializada como uma matriz identidade
    '''

    for i in range(len(M)):
        for j in range(len(M[i])):
            if j == i:
                M[i][j] = 1
            else:
                M[i][j] = 0


def neighborhood_on_lines(M, linha, coluna1, coluna2):

    '''
    Função auxiliar que retorna uma matriz obtida pela perturbação de um par de simbolos 
    de uma mesma linha, selecionados por parametro, sendo coluna1 < coluna2
    '''

    N = [[0 for i in range(len(M[0]))] for j in range(len(M))]

    elemento = M[linha][coluna1]

    for i in range(len(M)):
        for j in range(len(M[i])):

            if i == linha:
                if j == coluna1:
#                    print "coloquei ",M[i][coluna2]," no lugar de ",N[i][j]
                    N[i][j] = M[i][coluna2]

                elif j == coluna2:
#                    print "coloquei ",elemento," no lugar de ",N[i][j]
                    N[i][j] = elemento

                else:
#                    print "coloquei ",M[i][j]," no lugar de ",N[i][j]
                    N[i][j] = M[i][j]

            else:
#                print "coloquei ",M[i][j]," no lugar de ",N[i][j]
                N[i][j] = M[i][j]

    return N

def neighborhood_on_columns(M, coluna, linha1, linha2):

    '''
    Função auxiliar que retorna uma matriz obtida pela perturbação de um par de simbolos 
    de uma mesma coluna, selecionados por parametro, sendo linha1 < linha2
    '''

    N = [[0 for i in range(len(M[0]))] for j in range(len(M))]

    elemento = M[linha1][coluna]

    for i in range(len(M)):
        for j in range(len(M[i])):

            if i == linha1:
                if j == coluna:
                    N[i][j] = M[linha2][coluna]
                else:
                    N[i][j] = M[i][j]

            elif i == linha2:
                if j == coluna:
                    N[i][j] = elemento
                else:
                    N[i][j] = M[i][j]

            else:
                N[i][j] = M[i][j]

    return N


def neighbors(M):

    '''
    Função que retorna um array contendo os vizinhos do matching schema M
    '''

    list_neighbors = []

    for n in range(len(M)):
        for i in range(len(M[n])):
            for j in range(len(M[n])):
                if i != j:
                    elemento = neighborhood_on_lines(M,n,i,j)

                    #verificacao para nao colocar vizinhos repetidos, talvez dispensavel
                    if elemento not in list_neighbors:

                        list_neighbors.append(elemento)

    for m in range(len(M[0])):
        for i in range(len(M)):
            for j in range(len(M)):
                if i != j:
                    elemento = neighborhood_on_columns(M,m,i,j)

                    #verificacao para nao colocar vizinhos repetidos, talvez dispensavel
                    if elemento not in list_neighbors:

                        list_neighbors.append(elemento)

    return list_neighbors

#testes das funções
M = [[1,0,0,0],[0,1,0,0]]
print neighbors(M)
