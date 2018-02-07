#Gabriel Rodrigues Caldas de Aquino - gabriel@labnet.nce.ufrj.br
#Universidade Federal do Rio de Janeiro
#****************************************************#
#Para rodar o Ubuntu precisa ter numpy e matplotlib
#Para instalar, executar no shell:
#sudo apt-get install python-numpy
#sudo apt-get install python-matplotlib

import numpy.random as np #Random samples generator
import math #Para raiz quadrada
import matplotlib.pyplot as plt #Para plotar o dataset
import matplotlib.mlab as mlab #Para plotar pdf da gaussiana


#Definindo as Funcoes
def media(dataset): #calcula media dos dados
	soma=0.0
	for i in range(0, len(dataset)):
		soma=soma+dataset[i]
	
	return soma/len(dataset)

def percentil(dataset, percentil): #retorna o percentil da massa de dados P50, P90, etc...

        index=(len(dataset) * (percentil / 100.0))
        return dataset[int(index)]

def curtose(dataset): #curtose
	p25=percentil(dataset, 25)       
	p75=percentil(dataset, 75)
	
	p90=percentil(dataset, 90)
	p10=percentil(dataset, 10)
        
	cima=(p75 - p25)
        
	if(cima == 0):
		return 0.0

	baixo=(p90 - p10)

	return (0.5) * (cima/baixo)

def desvioPadrao(dataset): #desvio padrao 
	media_local=0.0
	media_local=media(dataset)
	soma=0

	for i in range(0, len(dataset)):
		soma=(soma + ( (dataset[i] - media_local) * (dataset[i] - media_local) ) )

	variance=(soma/( len(dataset) - 1.0) )
	
	return math.sqrt(variance)

def assimetria(dataset): #calcula assimetria

	media_local=media(dataset)
	p50=percentil(dataset, 50)
	sd=desvioPadrao(dataset)

	CTE3=3.0

	cima=(media_local - p50)

	if(cima == 0.0):
		return 0.0

	return CTE3 * (cima/sd)

def plotar(dataset): #Plotar o dataset
	bins=200 #quantidade de celulas
	plt.hist(dataset, bins, alpha=0.5)
	plt.title("Histogram")
	plt.xlabel("Value")
	plt.ylabel("Frequency")

	plt.show()


###PROGRAMA###

#Parametros da curva gaussiana a ser amostrada
mean=0.0
standardDeviation=1
Nsamples=10000

#Parametros da curva gaussiana que sera misturada
mean_mistura=10.0
standardDeviation_mistura=1
Nsamples_mistura=10000

#Criando o array que guardara as N amostras
dataset=[]

#Retirando N amostras da gaussiana com os parametros
for x in range(0, Nsamples):
	dataset.append( np.normal(mean, standardDeviation) )

#Colocando outliers no dataset (misturando), para verificar como que a curtose e a assimetria se comportam
for x in range(0, Nsamples_mistura):
	dataset.append(np.normal(mean_mistura, standardDeviation_mistura))

#Como vou analisar curtose e assimetria por quartis, devo ordenar o vetor
dataset.sort()


print 'Mean: ' + str(media(dataset))
print 'Kurtosis: ' + str(curtose(dataset))
print 'Skewness: ' + str(assimetria(dataset))

plotar(dataset)


