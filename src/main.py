import csv
from sklearn.cluster import spectral_clustering
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

import sys

gamma = 0.9
clusters = 3
colors = ['r', 'g', 'b', 'y', 'm', 'k']
# Min/Max of each parameter
BENZ = (sys.float_info.max, sys.float_info.min)
TEMP = (sys.float_info.max, sys.float_info.min)
UMID = (sys.float_info.max, sys.float_info.min)

def get_data_from_row(row):
    global BENZ, TEMP, UMID
    # Get Benzene, Temperature and humidity
    try:
        benz = float(row[5])
        auxB = list(BENZ)
        if benz < auxB[0]:
            auxB[0] = benz
        if benz > auxB[1]:
            auxB[1] = benz
        BENZ = tuple(auxB)

        temp = float(row[12])
        auxT = list(TEMP)
        if temp < auxT[0]:
            auxT[0] = temp
        if temp > auxT[1]:
            auxT[1] = temp
        TEMP = tuple(auxT)

        umid = float(row[14])
        auxU = list(UMID)
        if umid < auxU[0]:
            auxU[0] = umid
        if umid > auxU[1]:
            auxU[1] = umid
        UMID = tuple(auxU)

        return np.array([benz, temp, umid])
    except ValueError as e:
        print("error => \"", e, "\" Benz: ",row[5],"| Temp: ",row[12], "| Umid: ",row[15])

def affinity(mat):
    size = int(mat.size / 3)
    print(size)
    aff = np.zeros((size, size))
    for i in range(0, size):
        for j in range(0, size):
            if i > j :
                aff[i][j] = aff[j][i]
            else:
                d0 = abs(mat[i][0] - mat[j][0])
                d1 = abs(mat[i][1] - mat[j][1])
                d2 = abs(mat[i][2] - mat[j][2])
                d = np.sqrt(d0**2 + d1**2 + d2**2)
                aff[i][j] = np.exp(-(d/(2*gamma**2)))

    return aff

def main():
    with open('../data/AirQualityUCI.csv') as csvfile:
        # Parse CSV
        data = csv.reader(csvfile, delimiter=';', quotechar='|')
        size = sum(1 for _ in data)
        csvfile.seek(0)
        data = csv.reader(csvfile, delimiter=';', quotechar='|')

        # Create data matrix
        data_matrix = np.empty((size, 3))
        i = 0
        for row in data:
            data_matrix[i] = get_data_from_row(row)
            i += 1

        # Create affinity matrix
        aff = affinity(data_matrix)
        print(aff)

        label_im = -np.ones(aff.shape)
        # MAGIC
        labels = spectral_clustering(aff, n_clusters = clusters, eigen_solver = 'arpack')
        label_im[1] = labels
        print(labels)

        # Print Affinity Matrix
        plt.matshow(aff)

        # Print plotted data
        fig = plt.figure()
        ax_orig = Axes3D(fig)
        ax_orig.set_xlabel("Benzeno")
        ax_orig.set_ylabel("Temperatura")
        ax_orig.set_zlabel("Umidade abs")
        ax_orig.scatter(data_matrix[:, 0], data_matrix[:, 1], data_matrix[:, 2])

        # Print clusteres plotted data
        fig1 = plt.figure()
        ax_clstrd = Axes3D(fig1)
        ax_clstrd.set_xlabel("Benzeno")
        ax_clstrd.set_ylabel("Temperatura")
        ax_clstrd.set_zlabel("Umidade abs")
        i = 0
        for data in data_matrix:
            ax_clstrd.scatter(data[0], data[1], data[2], c=colors[labels[i]], depthshade=True)
            i += 1

        plt.show()

if __name__ == "__main__":
    main()