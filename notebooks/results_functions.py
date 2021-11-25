import numpy as np
import matplotlib.pyplot as plt
from LMDPs.plotting import plot_as_matrix as plotmat
import pickle
from mpl_toolkits.axes_grid1 import make_axes_locatable

def get_MAE_HL_errors(path, title, xlim, ylim=1, figsize=(7,7), plot_only=[], key=None):
    f = open(path,'rb')
    d = pickle.load(f)
    plt.close('all')
    
    fig, ax = plt.subplots(1,1, figsize=figsize)
    
    
    auxiliary_d = {}
    for k in d:
        auxiliary_d[k] = min(d[k][2])
        
    min_combination_c0_c1 = min(auxiliary_d, key=auxiliary_d.get)

    ax.set_title(f'{title}. Min.error with {min_combination_c0_c1}')

    colormap = plt.cm.gist_ncar
    plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, len(d)))))
        
    plotted = []
    for k in d:
        
        if plot_only and k not in plot_only:
            continue 
        else:
            Z, Z_subtasks, errors, errors_i = d[k]
            ax.plot(errors, linewidth=1, markevery=25)
            
        plotted.append(k)

    ax.legend([f'c={key} min = {min(d[key][3]):1.3E}' for key in plotted], fontsize=6)
    ax.set_xlim((0,xlim))
    ax.set_ylim((0,ylim))
    ax.set_ylabel('error')
    ax.set_xlabel('n_samples')

    
    if key is None:
        return d[min_combination_c0_c1]
    else:
        return d[key]
        
def get_MAE_plain_Z_learning(path, title, xlim, ylim):
    
    aux = pickle.load(open(path, 'rb'))
    res = {k:aux[k][1] for k in aux}
    
    fig, ax = plt.subplots(1,1)

    colormap = plt.cm.gist_ncar
    plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, len(res)))))
    
    
    st = {k:min(res[k]) for k in res}
    min_c = min(st, key=st.get)
    
    ax.set_title(f'{title}. Min.error with {min_c}')

    
    for k in res:

        errors = res[k]
        ax.plot(errors, linewidth=1, markevery=25)

    ax.legend([f'c={key} min = {min(res[key]):1.3E}' for key in res], fontsize=8)
    ax.set_xlim((0,xlim))
    ax.set_ylim((0,ylim))
    ax.set_ylabel('error')
    ax.set_xlabel('n_samples')

    return res[min_c]


def get_MAE_LL_errors(path, title, xlim, ylim=1, figsize=(7,4)):
    f = open(path,'rb')
    d = pickle.load(f)
    plt.close('all')
    
    fig, ax = plt.subplots(1,1, figsize=figsize)
       
    ax.set_title(f'{title}')

    colormap = plt.cm.gist_ncar
    plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, len(d)))))
    
    for k in d:
        
        Z, Z_subtasks, errors, errors_i = d[k]
                
        ax.plot(errors_i, linewidth=1, markevery=25)

    ax.legend([f'c={key} min = {min(d[key][3]):1.3E}' for key in d], fontsize=6)
    ax.set_xlim((0,xlim))
    ax.set_ylim((0,ylim))
    ax.set_ylabel('error')
    ax.set_xlabel('n_samples')


def plot_taxi(Z, states, key, dim, title, figsize=(5, 10), annotated=False, save_path=None):
    k1, k2 = key

    rs1 = [s for s in states if s[1] == k1 and s[2] == k2]
    rs1 = sorted(rs1, key=lambda x: (x[0][1], x[0][0]))
    rs1_idxs = list(map(states.index, rs1))

    V1 = np.log(Z[rs1_idxs])

    rs2 = [s for s in states if s[1] == 'TAXI' and s[2] == k2]
    rs2 = sorted(rs2, key=lambda x: (x[0][1], x[0][0]))
    rs2_idxs = list(map(states.index, rs2))

    V2 = np.log(Z[rs2_idxs])

    fig = plt.figure(figsize=figsize)

    ax1 = fig.add_subplot(1, 2, 1, aspect="equal")
    ax2 = fig.add_subplot(1, 2, 2, aspect="equal")

    im1 = ax1.matshow(V1.reshape(dim, dim), cmap=plt.get_cmap('magma'), vmin=V1.min(), vmax=V2.max())
    im2 = ax2.matshow(V2.reshape(dim, dim), cmap=plt.get_cmap('magma'), vmin=V1.min(), vmax=V2.max())

    divider1 = make_axes_locatable(ax1)
    cax1 = divider1.append_axes("right", size="5%", pad=0.3)

    divider2 = make_axes_locatable(ax2)
    cax2 = divider2.append_axes("right", size="5%", pad=0.3)

    # Create and remove the colorbar for the first subplot
    cbar1 = fig.colorbar(im1, cax=cax1)
    fig.delaxes(fig.axes[2])

    # Create second colorbar
    cbar2 = fig.colorbar(im2, cax=cax2, ticks=[V1.min() + 1, V2.max() - 1])

    # cbar.ax.tick_params(size=0)
    cbar2.ax.set_yticklabels(['Low $\hat V(s)$', 'High $\hat V(s)$'])

    plt.tight_layout()

    text = ax1.text(k1[0], k1[1], 'P', ha="center", va="center", color="w")
    text = ax2.text(k2[0], k2[1], 'D', ha="center", va="center", color="b")

    fig.suptitle(f'{title}', y=0.75)

    if save_path is not None:
        plt.savefig(f'{save_path}.pdf', bbox_inches='tight', dpi=500)

    return fig


def plot_gridworld(V, title, figsize=(10, 10), annotated=False, save_path=None):
    fig = plt.figure(figsize=figsize)

    ax = plt.gca()

    # axes = figure.add_subplot(111)
    # axes.set_title(f'{title}')
    caxes = ax.matshow(V, interpolation='nearest')
    ax.set_title(title)

    # axes.plot([-0.5, 1.5], [4.5, 4.5], color='black', linewidth='3')
    # axes.plot([4.5, 4.5], [-0.5, 4.5], color='black', linewidth='3')

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.3)

    cbar = fig.colorbar(caxes, cax=cax, ticks=[V.min() + 1, V.max() - 1])
    # cbar.ax.tick_params(size=0)
    cbar.ax.set_yticklabels(['Low $\hat V(s)$', 'High $\hat V(s)$'])

    # fig.suptitle(f'{title}', y=0.91)

    plt.tight_layout()

    if annotated:
        for i in range(V.shape[0]):
            for j in range(V.shape[1]):
                text = ax.text(j, i, f'{V[i, j]:.2f}', ha="center", va="center", color="w")

    if save_path is not None:
        plt.savefig(f'{save_path}.pdf', bbox_inches='tight', dpi=500)

    return fig