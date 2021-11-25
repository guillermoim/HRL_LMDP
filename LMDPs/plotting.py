import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def plot_Z_function(title, N_DIM, Z, log_Z, label_Z='Z', label_log_Z='-log(Z)'):
    X = np.arange(0, N_DIM, 1)
    Y = np.arange(0, N_DIM, 1)
    X, Y = np.meshgrid(X, Y)

    plt.close('all')
    fig = plt.figure(figsize=plt.figaspect(.5))
    ax = fig.add_subplot(1, 2, 1, projection='3d', title=f'{title}')
    ax.plot_surface(Y, X, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax.set_xlabel('Y')
    ax.set_ylabel('X')
    ax.set_zlabel(label_Z)

    ax1 = fig.add_subplot(1, 2, 2, projection='3d', title=f'{title}')
    ax1.plot_surface(Y, X, log_Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax1.set_xlabel('Y')
    ax1.set_ylabel('X')
    ax1.set_zlabel(label_log_Z)

    return fig


def plot_as_matrix(V, title, figsize=(10,10), annotated=False, save_path=None):

    figure = plt.figure(figsize=figsize)
    axes = figure.add_subplot(111)
    axes.set_title(f'{title}')
    caxes = axes.matshow(V, interpolation='nearest')

    #axes.plot([-0.5, 1.5], [4.5, 4.5], color='black', linewidth='3')
    #axes.plot([4.5, 4.5], [-0.5, 4.5], color='black', linewidth='3')

    #cbar = figure.colorbar(caxes, [V.min(), V.max()])
    #cbar.ax.set_xticklabels([str(V.min()), str(V.max())])

    if annotated:
        for i in range(V.shape[0]):
            for j in range(V.shape[1]):
                text = axes.text(j, i, f'{V[i, j]:.2f}', ha="center", va="center", color="w")

    if save_path is not None:
        plt.savefig(f'{save_path}.png', bbox_inches='tight')

    return figure