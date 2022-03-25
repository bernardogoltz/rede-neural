import numpy as np
np.random.seed(0)

linhas = 2
colunas = 3
X  = np.random.randn(linhas,colunas)

def sigmoide(x):
    return 1/(1-np.exp(-x))

#betas = np.random.rand(linhas)
#pesos = np.random.randn(colunas , linhas)

class Layer_Dense:
    
    def __init__(self , n_colunas , n_neuronios):
        
        self.pesos = np.random.randn(n_colunas , n_neuronios)
        self.betas = np.zeros((1,n_neuronios))
        
    def propaga(self, inputs):
        self.output = sigmoide(np.dot(inputs , self.pesos)+self.betas)
         
camadas = int(input("Camadas: "))

for i in range(camadas):
    
    idx = str(i+1)
    camada_indice = "camada"+idx
    
    neuronios = int(input("neurônios camada {}: ".format(idx)))
    camada = Layer_Dense(colunas, neuronios)
    camada.propaga(X)
    print(camada_indice)
    print(camada.output)
    
    colunas = neuronios
    X = camada.output
