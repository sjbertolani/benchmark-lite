
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

df = pd.read_csv('score.sc',header=0, sep='\s+')


# In[3]:

interfcst = 'SR_6_interf_E_1_3'
cst_filtered = df[ df.allcst < 55 ]
lowetotalscore = cst_filtered.sort_values('total_score').head(10)
print lowetotalscore.sort_values(interfcst)[['description','allcst','total_score',interfcst]].head(5)

