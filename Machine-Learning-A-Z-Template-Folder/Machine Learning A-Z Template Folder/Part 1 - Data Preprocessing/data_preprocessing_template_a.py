# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 19:03:44 2017

@author: David Harcourt
"""
# Data Preprocessing

# Importing the Libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values