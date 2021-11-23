#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 13:38:09 2021

@author: P.Chimenti, B.Araujo, R.Bassi
"""

from Models import Poisson

Measurement = 0
ConfidenceLevel = 0.95

UpperLimit = Poisson.UpperLimit(Measurement, ConfidenceLevel)
print(UpperLimit)

