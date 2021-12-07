#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: P.Chimenti, B.Araujo, R.Bassi
"""


import numpy as np
import scipy.stats as st
import pandas as pd
import time

def main():

    start_time = time.time()


    real = 50

    confidence = 90/100

    numberofsamples = 10000

    data = []
    data2 = []

    for sample in range(numberofsamples):

        # Simulation of Data
        simulatedparameter = float(st.poisson.rvs(real, loc=0, size=1))


        # Alternative Calculation
        step = 0.01
        param_points     = np.arange(0+step,100+step, step)
        min_value_points = [ st.poisson.ppf(1-(1+confidence)/2, mu=val) for val in param_points ]
        max_value_points = [ st.poisson.ppf(1-(1-confidence)/2, mu=val) for val in param_points ]
        
        confidence_points = []
        for i in range(len(param_points)):
            if min_value_points[i] <= simulatedparameter and max_value_points[i] >= simulatedparameter:
                confidence_points.append(param_points[i])

        dots_x = np.ones(len(confidence_points))*simulatedparameter
        dots_y = np.array(confidence_points)

        data2.append([simulatedparameter,dots_y[0],dots_y[-1]])
        df2=pd.DataFrame(data2,columns=["parameter","minconfidence","maxconfidence"])
    
    
        print("{0} - {1} minutes ---".format(sample,((time.time() - start_time)/60)))


    #print(data)
    print(df)
    print(df2)


def UpperLimit(Measurement, ConfidenceLevel):
    """ It return the upper limit with a 10^-2 precision  """
    step  = 0.01  # arbitrary for now, let the user define it
    limit = step
    while True :
        if st.poisson.ppf( 1-ConfidenceLevel, mu=limit) > Measurement : break
        limit+=step
    return limit

def Central(Measurement, ConfidenceLevel):
    
    return 0,0

def FeldmanCousins(Measurement, ConfidenceLevel):
    
    return 0,0


if __name__ == "__main__":
    main()
