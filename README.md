# Voroni-Scatter
Using a Voroni diagram to represent 2d scatter data

```

import seaborn.apionly as sns # only used for the iris dataset
import voroni
fig,(ax1,ax2)= plt.subplots(1,2,figsize=(16,5)) # creates a figure with two subplots (ax1,ax2)
iris = sns.load_dataset('iris') # loads a standard iris dataset
scatter_vor(iris,
            x='sepal_length',
            y='sepal_width',
            c='petal_length',
            ax=ax1) # generates the voronoi plot
iris.plot.scatter(	x='sepal_length',
            y='sepal_width',
            c='petal_length',
            cmap='jet',
            colorbar=False,
            ax=ax2) # generates a standard scatter plot

plt.show() # shows plot in the xserver
```
