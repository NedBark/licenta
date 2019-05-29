import matplotlib
import cv2
import numpy as np
import ast
import matplotlib.pyplot as plt
import math

def medie(x):
    medie = np.sum(x) / len(x)
    return medie

f = open('vectors', 'r')

haar = f.readline()
haar = ast.literal_eval(haar)

lbp = f.readline()
lbp = ast.literal_eval(lbp)

nplbp = np.copy(lbp)
nphaar = np.copy(haar)
nphaar[nphaar[:,0]<100] = [500,200]

lbp_medie_y = medie(nplbp[:,1])
dif = nphaar - nplbp

haar_medie_y = medie(nphaar[:,1])

medie_x = np.sum(dif, axis=0) / len(dif)
medie_y = np.sum(dif, axis=1) / len(dif)
medie_y = np.sum(medie_y, axis=0)
nhaar = nphaar - medie_y

abatere_lbp = np.sum((nplbp[:, 1] - lbp_medie_y)**2) / len(dif-1)

abatere_haar = np.sum((nphaar[:, 1] - haar_medie_y)**2) / len(dif-1)



plt.plot(nplbp[:, 0], nplbp[:, 1], 'bx')
plt.plot(nphaar[:, 0], nphaar[:, 1], 'rx')
plt.ylabel('Picture height [pixels]')
plt.xlabel('Picture width [pixels]')
plt.grid(True)
plt.legend(['LBP - ' + str(round(abatere_lbp, 5)) + ' (deviation)', 'Haar - ' + str(abatere_haar) + ' (deviation)'])

# plt.axis([0, 640, 0, 480])
plt.show()
