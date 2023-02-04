#!/usr/bin/env python
# coding: utf-8

# # Bar Plot

# In[38]:


import matplotlib.pyplot as plt
x=["python","c","c++","java"]
y=[85,70,60,82]
z=[20,30,50,40]
plt.xlabel("programming languages",fontsize=10)
plt.ylabel("popularity percent")
plt.title("Popularity of Languages",fontsize=15)
c=["y","b","m","b"]
plt.bar(x,y, width=0.5, color=c, align="center",edgecolor="black",linewidth=5, linestyle="dotted",alpha=0.8,label="popularity")
plt.bar(x,z, width=0.5, color="red", align="center",alpha=0.8,label="popularity")
plt.legend()
plt.show()


# In[56]:


import matplotlib.pyplot as plt
import numpy as np
x=["python","c","c++","java"]
y=[85,70,60,82]
z=[20,30,50,40]

width=0.2
p=np.arange(len(x))
p1=[j+width for j in p]

plt.xlabel("programming languages",fontsize=10)
plt.ylabel("popularity percent")
plt.title("Popularity of Languages",fontsize=15)

plt.bar(p,y,  width,color="r",alpha=0.8,label="popularity")
plt.bar(p1,z,  width,color="y",alpha=0.8,label="popularity")

plt.xticks(p+width/2,x,rotation="10")
plt.legend()
plt.show()


# In[57]:


import matplotlib.pyplot as plt
x=["python","c","c++","java"]
y=[85,70,60,82]
z=[20,30,50,40]

plt.xlabel("programming languages",fontsize=10)
plt.ylabel("popularity percent")
plt.title("Popularity of Languages",fontsize=15)

c=["y","b","m","b"]
plt.barh(x,y, color=c, align="center",edgecolor="black",linewidth=5, linestyle="dotted",alpha=0.8,label="popularity")
plt.barh(x,z, color="red", align="center",alpha=0.8,label="popularity")

plt.legend()
plt.show()


# In[ ]:




