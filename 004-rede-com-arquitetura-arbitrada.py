"""
Created on Wed Mar 16 15:39:11 2022
==========================================

@author: bernardogoltz

@title: Rede Neural com M camadas e N neuronios por camada. 

"""

import numpy as np
np.random.seed(0)

linhas = 2
colunas = 3

X = np.random.randn(linhas,colunas)
# define randomicamente uma matriz de dados tabulados em dimensões arbitradas. 

def sigmoide(x):
    return 1/(1-np.exp(-x))
    # função de ativação.

#betas = np.random.rand(linhas)
#pesos = np.random.randn(colunas , linhas)

class Layer_Dense:
    
    def __init__(self , n_colunas , n_neuronios):
        
        self.pesos = np.random.randn(n_colunas , n_neuronios)
        # 1 peso pra cada elemento de uma linha, M neuronios pra cada linha. 
        
        self.betas = np.zeros((1,n_neuronios))
        # vieses = 1 vies p/ cada neuronio. 
        
    def propaga(self, inputs):
        self.output = sigmoide(np.dot(inputs , self.pesos)+self.betas)
         
camadas = int(input("Camadas: "))

for i in range(camadas):
    
    idx = str(i+1)
    # armazena o indice da camada 
    
    camada_indice = "camada"+idx
    # nomeia a camada iterada 
    
    neuronios = int(input("neurônios camada {}: ".format(idx)))
    # associa a camada com a quantidade de neurônio. 
    
    camada = Layer_Dense(colunas, neuronios)
    # variável que cria uma instância na classe 
    # Layer Dense com o numero de colunas da matriz         inicial e o numero de neuronios desejados por camada. 
    
    camada.propaga(X)
    # executa o método que faz a combinação linear entre cada linha da tabela e cada matriz coluna de pesos de cada neurônio. 
    
    print(camada_indice)
    # imprime o "nome" da camda. 
    
    print(camada.output)
    # imprime o resultado. 
    
    colunas = neuronios
    X = camada.output
    # ao final de cada combinação, enquanto o indice nao percorrer toda a quantidade de camadas inserida, é gerada uma nova matriz na qual as colunas serão os neurônios e a matriz a ser ponderada será o output da última camda calculada. 
