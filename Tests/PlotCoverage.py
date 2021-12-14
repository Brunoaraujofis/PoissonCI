# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 13:49:34 2021

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from Models import Poisson


def Coverage_Upper(mu):
    number_of_samples = 100
    success = 0
    for sample in range(number_of_samples):
        simulated_value = float(stats.poisson.rvs(mu, loc=0, size=1))
        upper_limit = Poisson.UpperLimit(simulated_value, ConfidenceLevel = 0.95)
        if upper_limit >= mu:
            success += 1
    return success/number_of_samples

param_points = [0.1]
L = list(np.arange(1.0, 11.0, 1))

for i in np.arange(10):
    param_points.append(L[i])

Coverage = []

for i in np.arange(len(param_points)):
    Coverage.append(Coverage_Upper(param_points[i]))
    
plt.plot(param_points, Coverage)
    
