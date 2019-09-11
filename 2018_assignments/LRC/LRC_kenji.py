
# coding: utf-8

# In[1]:


import numpy as np
get_ipython().run_line_magic('matplotlib', 'notebook')
import matplotlib.pyplot as plt


# In[2]:


data = np.loadtxt("lrc.txt", skiprows=3)


# In[13]:


#plt.plot(data[:,0],data[:,1])
plt.plot(data[:,0],data[:,1])
plt.title("Freq vs. Gain")
plt.xlabel("Frequency(Hz)")
plt.ylabel("Gain(dB)")


# In[7]:


get_ipython().run_line_magic('pinfo', 'plt.plot')

