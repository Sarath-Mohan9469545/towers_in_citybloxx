import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

def plot_city(l):
    cmap=colors.ListedColormap(["blue","red","green","yellow"])
    bounds=[0,10,20,30,40]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    plt.figure(frameon=True)

    lenofm=len(l)
    data=np.arange(lenofm*lenofm).reshape(lenofm,lenofm)

    for i in range(1,6):
        for j in range(1,6):
            if l[i][j]=="b":
                data[i-1][j-1]=5
            elif l[i][j]=="r":
                data[i-1][j-1]=15
            elif l[i][j]=="g":
                data[i-1][j-1]=25
            elif l[i][j]=="y":
                data[i-1][j-1]=35

    data=np.array(data)
    grid=True
    labels=False

    if grid:
        plt.grid(axis='both', color='k', linewidth=2) 
        plt.xticks(np.arange(0.5, data.shape[1], 1))  # correct grid sizes
        plt.yticks(np.arange(0.5, data.shape[0], 1))

    # disable labels
    if not labels:
        plt.tick_params(bottom=False, top=False, left=False, right=False, labelbottom=False, labelleft=False) 
    # plot data matrix
    plt.imshow(data, cmap=cmap, norm=norm)

    # display main axis 
    plt.show()






