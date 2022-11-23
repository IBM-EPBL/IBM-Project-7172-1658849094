# -*- coding: utf-8 -*-
"""data_preprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wNT_4ZMsGJ5at3vC4dGscY9FT7LjJmf4
"""

from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv(r'/content/Fertilizer Prediction.csv')

df.head()

df.tail()

df.size

df.shape

df.columns

df.describe()

df.dtypes