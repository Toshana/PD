# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 12:02:56 2016

@author: centraltendency
"""

import pandas as pd
import random


## import csv

trump = pd.read_csv("~/PD/trump_speech_one", sep = ",", header = 0)
trump["frequency"]=trump["count"].astype("int")
trump = trump.drop(trump.columns[[0, 2]], axis = 1)

h = 1000
w = 900

x_one = random.sample(range(1, 900), 891)
y_one = random.sample(range(1, 1000), 891)
x_two = random.sample(range(1, 900), 891)
y_two = random.sample(range(1, 1000), 891)

size = []
for i in (trump["frequency"]):
    size.append(i + 15)
    
trump["size"] = size
trump["x_one"] = x_one
trump["y_one"] = y_one
trump["x_two"] = x_two
trump["y_two"] = y_two

sorted_trump = trump.sort(["frequency"], ascending = False)

sorted_trump.to_csv("trump_d3_ex", sep = ",")