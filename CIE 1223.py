#!/usr/bin/env python
# coding: utf-8

# In[10]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
df = pd.read_csv("C:/Users/poorvika/Downloads/mtcars.csv")

plt.hist(df['mpg'])
plt.title('Histogram of MPG')
plt.xlabel('MPG')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

hist, bin_edges = np.histogram(df['mpg'], bins=10)
max_freq_bin = bin_edges[np.argmax(hist)]
print(max_freq_bin)  


# In[11]:


import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("C:/Users/poorvika/Downloads/mtcars.csv")

plt.scatter(df['wt'], df['mpg'])
plt.title('Scatter Plot of Weight vs MPG')
plt.xlabel('Weight (1000 lbs)')
plt.ylabel('MPG')
plt.grid(True)
plt.show()


# In[13]:


import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("C:/Users/poorvika/Downloads/mtcars.csv")

transmission_counts = df['am'].value_counts()
transmission_labels = ['Automatic', 'Manual']

plt.bar(transmission_labels, transmission_counts, color=['green', 'black'])
plt.title('Frequency Distribution of Transmission Types')
plt.xlabel('Transmission Type')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# In[14]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/poorvika/Downloads/mtcars.csv")

plt.boxplot(df['mpg'], vert=False, patch_artist=True)

plt.title('Box Plot of MPG')
plt.xlabel('Miles Per Gallon (MPG)')

plt.show()

five_number_summary = df['mpg'].describe()[['min', '25%', '50%', '75%', 'max']]
five_number_summary


# In[ ]:




