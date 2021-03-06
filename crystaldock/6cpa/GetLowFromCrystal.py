
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

df = pd.read_csv('score.sc',header=0, sep='\s+')


# In[3]:

interfcst = 'SR_10_interf_E_1_3'
metalcst = 'SR_9_interf_E_1_2'
cst_filtered = df[ df.allcst < 5 ]
lowetotalscore = cst_filtered.sort_values('total_score').head(5)
print lowetotalscore.sort_values(interfcst)[['description','allcst','total_score',interfcst,metalcst]].head(5)

