
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
def scatter_vor(data,x,y,c,cmap='jet',ax=None):
    cmap = plt.get_cmap(cmap)
    points= data[[x,y]].values
    color = data[c].values
    color = color - np.nanmin(color)
    color = color / np.nanmax(color)
    # compute Voronoi tesselation
    xLIM = (data[x].min(),data[x].max())
    xDist= xLIM[1]-xLIM[0]
    yLIM = (data[y].min(),data[y].max())
    yDist= yLIM[1]-xLIM[0]
    xDist,yDist=[i*10 for i in [xDist,yDist]]
    added_points=[]
    steps = 20
    added_points += [(xLIM[0]-xDist,i)for i in np.linspace(yLIM[0]-yDist,yLIM[1]+yDist,num = steps)]
    added_points += [(xLIM[1]+xDist,i)for i in np.linspace(yLIM[0]-yDist,yLIM[1]+yDist,num = steps)]
    added_points += [(i,yLIM[0]-yDist)for i in np.linspace(xLIM[0]-xDist,xLIM[1]+xDist,num = steps)]
    added_points += [(i,yLIM[1]+yDist)for i in np.linspace(xLIM[0]-xDist,xLIM[1]+xDist,num = steps)]
    added_colors  = np.array([sum(color)/len(color)]*len(added_points))
    added_points  = np.array(added_points)
    points = np.concatenate([points,added_points],axis=0)
    color  = np.concatenate([color ,added_colors],axis=0)
    vor = Voronoi(points, qhull_options='Qbb Qc Qx')
    # plot
    if ax==None:
        fig,ax=plt.subplots(1)
    voronoi_plot_2d(vor,ax=ax,show_points=False,show_vertices=False,line_alpha=0.0)
    ax.set_ylim(yLIM)
    ax.set_xlim(xLIM)
    # colorize
    ax.set_ylabel(y)
    ax.set_xlabel(x)
    for n,region in enumerate(vor.regions):
        if not -1 in region:
            c=color[np.where(vor.point_region == n)[0][0]]
            c=cmap(c)
            polygon = [vor.vertices[i] for i in region]
            ax.fill(*zip(*polygon),color=c)
    return ax

scatter_vor.py
Displaying scatter_vor.py.
