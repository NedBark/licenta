import matplotlib
import cv2
import numpy as np
import ast
import matplotlib.pyplot as plt


f = open('vectors', 'r')

haar = f.readline()
haar = ast.literal_eval(haar)

lbp = f.readline()
lbp = ast.literal_eval(lbp)

nplbp = np.copy(lbp)
nphaar = np.copy(haar)
dif = nplbp - nphaar

medie = np.sum(dif, axis=0) / len(dif)

plt.plot(nplbp[:, 0],nplbp[:, 1], 'bx')
plt.plot(nphaar[:, 0], nphaar[:, 1], 'rx')
# plt.axis([0, 640, 0, 480])
plt.show()
