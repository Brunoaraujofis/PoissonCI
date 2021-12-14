#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 13:38:09 2021

@author: P.Chimenti, B.Araujo, R.Bassi
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from Models import Poisson


def Coverage_Upper(mu):
    print("Coverage ",mu)
    number_of_samples = 10
    number_of_iterations = 8
    success = np.zeros(number_of_iterations)
    
    for iteration in range(number_of_iterations):
        for sample in range(number_of_samples):
            simulated_value = float(stats.poisson.rvs(mu, loc=0, size=1))
            upper_limit = Poisson.UpperLimit(simulated_value, ConfidenceLevel = 0.95)
            if upper_limit >= mu:
                success[iteration] += 1
    mean_success = np.mean(success/number_of_samples)
    var_success = np.var(success/number_of_samples)
    return mean_success, np.sqrt(var_success)

param_points = [0.1]
L = list(np.arange(1.0, 11.0, 1))

for i in np.arange(10):
    param_points.append(L[i])

Coverage = []
Coverage_error = []

for i in np.arange(len(param_points)):
    result_coverage = Coverage_Upper(param_points[i]) 
    Coverage.append(result_coverage[0])
    Coverage_error.append(result_coverage[1])
    
plt.errorbar(param_points, Coverage, Coverage_error)
plt.show()    
