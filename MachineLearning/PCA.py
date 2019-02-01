import numpy as np
import matplotlib.pyplot as plt
import math
from copy import deepcopy


class PCA(object):

    def __init__(self, k=3, tolerancia=0.0001, max_iterations=500):
        self.k = k
        self.tolerancia = tolerancia
        self.max_iterations = max_iterations        

    def fit(self, data, n_clusters=3):        
        self.otimizado = False
        self.initialize_centroids(data)
        for _ in range(self.max_iterations):

            self.initialize_classes()    

            # Calcula a distancia entre os pontos e os clusters. Escolhe o cetroid mais proximo
            for sample in data:
                distances = [self.Distancia_Euclidiana(sample, centroid) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classes[classification].append(sample)
            
            self.recalcular_centroids()

            # Termina se estiver otimizado: se os centroids alteram pouco a posicao(menos que a tolerancia definida)	
            if self.otimizado:
                break    

                
    def initialize_centroids(self, data):
        self.centroids = []
        # Os primeiros 'k' elementos do dataset serão os centroids iniciais
        for i in range(self.k):
            self.centroids.append(data[i])
    
    def initialize_classes(self):
        self.classes = {}
        for i in range(self.k):
            self.classes[i] = []

    def recalcular_centroids(self):
        anterior = deepcopy(self.centroids)
        # Recalcula os centroids com base na média dos pontos do cluster
        for classification in self.classes:
            self.centroids[classification] = np.average(self.classes[classification], axis = 0)

        for i in range(len(self.centroids)):
            centroid_original = anterior[i]
            centroid_atual = self.centroids[i]
            if np.sum((centroid_atual - centroid_original)/centroid_original * 100.0) > self.tolerancia:
                self.otimizado = False


    def Distancia_Euclidiana(self, matriz_A, matriz_B):
        distancia = 0
        for i in range(len(matriz_A)):
            distancia += (matriz_A[i] - matriz_B[i]) ** 2
            ed = math.sqrt(distancia)
        return ed   
