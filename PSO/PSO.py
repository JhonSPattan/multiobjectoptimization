import numpy as np
import pandas as pd
import random
from Benchmark.Prototype import FunctionOptimization
from Util.Analysis import FileAnalysis


class PSO:

    cpVal = 0
    cgVal = 0
    round = 0
    replace = 0
    populationSize = 0
    dimensionSize = 0

    problemtype = ""
    algorithmname = ""
    functionname = ""
    functiontype = ""

    functionBenchmark = FunctionOptimization

    def __init__(self,functionBenckmark:FunctionOptimization,populationSize:int=100,dimensionSize:int=100,cpVal:float=0.5,cgVal:float=0.5,round:int=1000,replace:int=30,problemtype:str='Small',algorithmname:str="PSO",
                 functionname:str="None",functiontype:str="MultiObj") -> None:
        
        self.cpVal = cpVal
        self.cgVal = cgVal
        self.round = round
        self.replace = replace
        self.populationSize = populationSize
        self.dimensionSize = dimensionSize
        
        self.problemtype = problemtype
        self.algorithmname = algorithmname
        self.functionname = functionname
        self.functiontype = functiontype

        self.functionBenchmark = functionBenckmark(populationSize,dimensionSize)

        def generate(self)->np.array:
            return self.functionBenchmark.generate()


        def eveluate(self,individual)->np.double:
            return self.functionBenchmark.eveluate(individual)
        
        def generateVelocity(self)->np.array:
            return np.random.uniform(0,1,size=(self.populationSize,self.dimension))

        def updateVelocity(self,velocityIndividual:np.array,individual:np.array,bestpIndividual:np.array,bestgIndividual:np.array)->np.array:
            return velocityIndividual+self.cpVal*(bestpIndividual-individual)+self.cgVal*(bestgIndividual-individual)

        def updatePopulation(self,individual:np.array,velocityIndividual:np.array)->np.array:
            return individual+velocityIndividual
        

        def optimization(self)->np.array:
            bestIndividualList = []
            bestFitness = []
            roundValueplot = []
            for k in range(self.replace):
                
                population = self.generate()
                pBest = population
                velocity = self.generateVelocity()
                minValue = 9e+9
                minround = np.zeros(self.round)
                fitnessValue = np.zeros(self.dimensionSize)
                minIndex = 0
                bestPopulation = np.zeros(self.dimensionSize)
                for i in range(self.round):
                    for j in range(self.populationSize):
                        fitnessValue[i] = self.eveluate()

                    if minValue > min(fitnessValue) or i == 0:
                        minValue = min(fitnessValue)
                        minIndex = np.where(fitnessValue==minValue)[0]
                        bestPopulation = population[minIndex][0]

                    for j in range(self.populationSize):
                        velocity[j] = self.updateVelocity(velocity[j],population[j],pBest[j],bestPopulation)


                    # for j in range(self.populationSize):



            
            return np.array([3,4,5])

