import pandas as pd
import numpy as np
import scipy as sp
import matplotlib as mpl

data_csv=pd.read_csv('credit_immo\credit_immo.csv')
data_json=pd.read_json('credit_immo\credit_immo.json')
data_xls=pd.read_excel('credit_immo\credit_immo.xls')

df = pd.DataFrame(data_csv, index = ['1', '2', '3', '4','5','6'], columns = ['taux_de_ventes', 'croissance_vente', 'ratio_benefice', 'ratio_perte'])

code = df(np.zeros(df.shape[0]))
print(code.shape)