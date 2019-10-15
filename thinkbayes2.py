import bisect
import copy
import logging
import math
import numpy
import random
import matplotlib.pyplot as plt

import scipy.stats
from scipy.special import erf, erfinv
from thinkbayes import Pmf


class Suite(Pmf):
    
    def __init__(self, hypos=tuple()):
        super().__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()
    
    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()
    
    def Likelihood(self, data, hypo):
        
        raise UnimplementedMethodException()
    
    def Print(self):
        for hypo, prob in self.Items():
            print(hypo, prob)
    
    def plot(self):
        x = []
        y = []
        for hypo, prob in self.Items():
            x.append(hypo)
            y.append(prob)
        plt.plot(x, y)
        plt.show()
    
    def mean(self):
        total = 0
        for hypo, prob in self.Items():
            total += hypo * prob
        
        return total
    
    def Percentile(self, percentage):
        p = percentage/100
        total = 0
        for val, prob in self.Items():
            total += prob
            if total >= p:
                return val
            