#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np

fname = "C:\\Users\\katko\\Documents\\GitHub\\ses330\\SESE330-Youssef-Lab2datafile.txt"

x,y,z = np.loadtxt(fname, dtype=None, usecols=(0,1,2),unpack=True)
fig,ax = plt.subplots()
ax.plot(x,y)
ax.set(xlabel='Frequency(Hz)',ylabel='Gain(dB)',title='Frequecy vs Gain')
ax.grid()
plt.show()

fig,ax = plt.subplots()
ax.plot(x,z)
ax.set(xlabel='Frequency(Hz)',ylabel='Phase(deg)',title='Phase vs Frequency')
ax.grid()
plt.show()

