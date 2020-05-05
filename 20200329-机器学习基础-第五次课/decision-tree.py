"""
使用svm实现决策树
"""
import pandas as pd
import numpy as np

def load_data():
    df = pd.read_csv('./data_reg.csv')
    X = df[['AT', 'V', 'AP', 'RH']]
    y = df[['PE']]
