# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

def sigmoide(x):
    return 1/(1-np.exp(-x))
    
linhas = 3
colunas = 2


arquitetura = [
    {"dim_entrada":colunas , "dim_saida":linhas},
    {"dim_entrada":2 , "dim_saida":1}
    ]

def inicia_camadas(arquitetura):
    
    numero_de_camadas = len(arquitetura)
    valores_parametros = {}
    
    for indice, camada in enumerate(arquitetura):
        
        indice_camada = indice + 1
        
        tamanho_camada_entrada = camada["dim_entrada"]
        tamanho_camada_saida = camada["dim_saida"]
        
        valores_parametros['P'+str(indice_camada)] = np.random.randn(tamanho_camada_saida , tamanho_camada_entrada)
        
        valores_parametros['b'+str(indice_camada)] = np.random.randn(tamanho_camada_saida,1)
        
        return valores_parametros
    
def propaga_uma_camada(Ativado_anterior , Pesos_atual , b_atual):
    Saida_atual = np.dot(Pesos_atual , Ativado_anterior) + b_atual
    return sigmoide(Saida_atual) , Saida_atual

def propaga_total(X , valores_parametros , arquitetura):
    memoria = {}
    
    for indice, camada in range(len(arquitetura)):
        
        indice_camada = indice + 1 
        Ativado_anterior = Ativado_atual
        
        Pesos_atual = valores_parametros['P'+str(indice_camada)]
        b_atual = valores_parametros['b'+str(indice_camada)]
        
        Ativado_atual , Saida_atual = propaga_uma_camada(Ativado_anterior, Pesos_atual, b_atual)
        
        memoria["A"+str(indice)] = Ativado_anterior
        memoria["Z"+str(indice_camada)] = Saida_atual
    return Ativado_atual , memoria

valores_parametros = inicia_camadas(arquitetura)


    
        
        
    

