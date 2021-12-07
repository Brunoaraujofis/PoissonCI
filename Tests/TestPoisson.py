#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 13:38:09 2021

@author: P.Chimenti, B.Araujo, R.Bassi
"""

from Models import Poisson
import scipy.stats as st

def Coverage_Upper(mu, confidence):
    number_of_samples = 100
    success = 0
    for sample in range(number_of_samples):
        simulated_value = float(st.poisson.rvs(mu, loc=0, size=1))
        upper_limit = Poisson.UpperLimit(simulated_value, ConfidenceLevel)
        if upper_limit >= mu:
            success += 1
    return success/number_of_samples
        
        
true_value = 10
ConfidenceLevel = 0.95

print("Confidence covarage: mu = ", true_value, " confidence = ", ConfidenceLevel, " coverage = ", Coverage_Upper(true_value, ConfidenceLevel))

true_value = 1
ConfidenceLevel = 0.95

print("Confidence covarage: mu = ", true_value, " confidence = ", ConfidenceLevel, " coverage = ", Coverage_Upper(true_value, ConfidenceLevel))
