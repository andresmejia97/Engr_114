# data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_data(wd, w_type):
    # wd = np.array([32,33,34,36,42,44,45])
    n_data_pts = len(wd)
    d = {'temperature':'*F', 'pressure':'in. HG', 'rainfall':'in. per min.', 'humidity':'%'}
    y_label = f'{w_type} ({d[w_type]})'

    fig, ax = plt.subplots()
    ax.plot(wd)
    ax.set_title(f'Temperature in Natick, MA using {n_data_pts} data points')
    ax.set_xlabel('data points')
    ax.set_ylabel(f'{y_label}')

    plt.show()