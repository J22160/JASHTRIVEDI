#!/usr/bin/env python
# coding: utf-8

# In[8]:


import seaborn as sns
sns.set(style='ticks')
import matplotlib.pyplot as plt
import pandas as pd


# In[9]:


df=pd.read_csv('D:\data_eda.csv')
df


# In[10]:


plt.figure(figsize=(5.5, 5.5))

sns.countplot(x='bioactivity', data=df, edgecolor='black')

plt.xlabel('Bioactivity class', fontsize=14, fontweight='bold')
plt.ylabel('Frequency', fontsize=14, fontweight='bold')


# In[11]:


selection = ['canonical_smiles','molecule_chembl_id']
df3_selection = df[selection]
df3_selection.to_csv('for_padel.smi', sep='\t', index=False, header=False)


# In[17]:


df3_selection.to_csv('curr_data.csv',index=False)


# In[12]:


data=pd.read_csv('D:\datafinal_md.csv')
data


# In[13]:


data.describe()


# In[14]:


import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


# In[15]:


df3_X = data.drop(columns=['Name'])
df3_X


# In[20]:


y_data=pd.read_csv('D:\data_eda_ytrain.csv')
y_data


# In[23]:


data_y=y_data['pIC50']
data_y


# In[25]:


x=df3_X
x


# In[26]:


y=data_y
y


# In[27]:


from sklearn.feature_selection import VarianceThreshold
selection = VarianceThreshold(threshold=(.8 * (1 - .8)))    
x = selection.fit_transform(x)


# In[29]:


x.shape


# In[30]:


X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size=0.2)


# In[31]:


X_train.shape,Y_train.shape


# In[33]:


X_test.shape,Y_test.shape


# In[34]:


model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)


# In[35]:


r2 = model.score(X_test, Y_test)
r2


# In[47]:


from sklearn.metrics import r2_score


# In[49]:


score=r2_score(Y_test,Y_pred)
score


# In[55]:


sns.set(color_codes=True)
sns.set_style("white")

ax = sns.regplot(Y_test, Y_pred, scatter_kws={'alpha':0.4})
ax.set_xlabel('Experimental pIC50', fontsize='large', fontweight='bold')
ax.set_ylabel('Predicted pIC50', fontsize='large', fontweight='bold')
ax.set_xlim(3,12)
ax.set_ylim(3,12)
ax.figure.set_size_inches(10,10)
plt.show

