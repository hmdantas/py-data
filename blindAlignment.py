#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Implementação do algoritmo "Blind Alignment" publicado em:

Cauteruccio F., Fortino G., Guerrieri A., Terracina G. (2014) Discovery of Hidden Correlations between Heterogeneous Wireless Sensor Data Streams. In: Fortino G., Di Fatta G., Li W., Ochoa S., Cuzzocrea A., Pathan M. (eds) Internet and Distributed Computing Systems. IDCS 2014. Lecture Notes in Computer Science, vol 8729. Springer, Cham

'''


from random import shuffle
from copy import copy
from math import factorial

#variaveis para teste
str1 = "AAABCCDDCAA"
str2 = "EEFGHGGFHH"
align1 = [['A'],['B'],['C'],['D']]
align2 = [['E'],['G'],['H'],['F']]

def editdistance(str1, str2, align1, align2):
    """
    Se as strings forem de tamanhos diferentes, essa diferença está sendo preenchida com "-" ao final da menor string.
    (Isso claramente influencia no resultado!!!!)
    """
    dist = 0

    if(len(str1) < len(str2)):
        str1 = str1 + "-"*abs(len(str1) - len(str2))

    elif(len(str2) < len(str1)):
        str2 = str2 + "-"*abs(len(str1) - len(str2))

    for i in range(len(str1)):

        index = -1

        #preciso encontrar a letra str1[i] no align1
        for a in align1:
            index = index + 1
            if (str1[i] in a):
                break

        #agora se a letra str2[i] estiver dentro da lista align2[index] temos um match!
        if (str2[i] not in align2[index]):
            dist = dist + 1
            print "nao pareou ",str1[i]," com ",str2[i]," quando i = ",i

    return dist

def initialize(str1, p1):
    alfabeto = list(set(str1))
    align = []
    p = []
    for l in alfabeto:
        if(len(p) < p1):
            p.append(l)
        else:
            align.append(p)
            p = []
            p.append(l)
    if(len(p) == p1):
        align.append(p)
    return align


def blindAlignment(str1, str2, p1, p2, T):

    #separando o conjunto de simbolos da string 1 e 2
    align1 = initialize(str1, p1)

    align2 = initialize(str2, p2)
        
    t = 0
    mindist = editdistance(str1, str2, align1, align2)
    globaldist = mindist
    improved = True

    while(improved):

        improved = False

        #precisa implementar essa busca por vizinhos
        n = neighbors(align1, align2)

        for Ml in n:

            e = editdistance(str1, str2, Ml[0], Ml[1])

            if (e < mindist):

                mindist = e
                improved = True
                M = Ml

        if not improved:

            if mindlist < globaldist:

                globaldist = mindist
                improved = True
                t = 0

            elif (t < T):

                t = t + 1
                improved = True
                #precisa implementar essa inicializacao aleatoria
                aligns = randomSelect(align1, align2)
                mindist = editdistance(str1, str2, align2[0], aligns[1])

    return globaldist
