#Author:     Carl Carmoney
#Date:       Mar 08, 2015
#Subject:    CS495-35W Artificial Intelligence
#Professor:  Bruno A.
#
#Comments from various runs are below the sourcecode - maybe...if I remember.
#Assignment #5

from simpleai.search import SearchProblem, hill_climbing_random_restarts
import sys
import pdb
import random
import time

class KnapsackProblem(SearchProblem):

    def __init__(self,numObjects,maxWeight,weights,values):
        super(KnapsackProblem, self)
        self.weights = weights
        self.values  = values
        self.maxWeight = maxWeight
        self.numObjects = numObjects # is it not better compute num?
        #How can I set these as the initial values if not passed in?
        #self.weights = [4,6,5,5,3,2,4,8,1,5,3,7,2,5,6,3,8,4,7,2]
        #self.values  = [5,6,2,8,6,5,8,2,7,6,1,3,4,4,1,5,6,2,5,3]
        #self.maximum = 35
        #self.num_objects = len(self.weights)

    def generate_random_state(self):
        '''
        Create a random DNA string (...from existing, probably).
        '''
        return 

    def crossover(self):

    def mutate(self):

    def value(self, s):
        '''
        Determin the sequence's fitness.
        '''
        return

    def _weight(self, s):
        '''
        Calculates the entire weight of the knapsack given s[x] == Truthy
        '''
        total = 0
        for pos in range(0,len(s)):
            if s[pos] == True:
                total += self.weights[pos]
        return total

    def _valid(self, s):
        if _weight(self,s) <= self.maxWeight:
            return True
        else:
            return False





weights = [4,6,5,5,3,2,4,8,1,5,3,7,2,5,6,3,8,4,7,2]
values  = [5,6,2,8,6,5,8,2,7,6,1,3,4,4,1,5,6,2,5,3]
maximum = 35
num_objects = len(weights)
starttime = time.time()
problem = KnapsackProblem( num_objects,maximum,weights,values )
result = genetic(problem, iterations_limit=100, population_size=16,mutation_chance=0.10) 
endtime = time.time()
for i in result.path():
    print i
print('It took ' + str(endtime - starttime) + ' to compute this answer.')
