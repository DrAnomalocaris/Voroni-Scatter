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
![voroni example](/voroni.png)
The standard scatter plot provides similar information to the Voronoi plot, but the Voronoi plot more clearly highlights the surface gradient in petal length occurring with septal length (gradient in the bottom right) and also clearly marks the border between low petal length and the rest of the values (blue region in the top left).
Perhaps a frivolous benefit of using the Voronoi plot is that it is more aesthetically pleasing and fully removes the negative space of a plot giving visual information in a much more stark fashion.
