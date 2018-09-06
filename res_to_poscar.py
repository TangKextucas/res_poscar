import pandas as pd
import numpy as np
from math import*
from collections import Counter
from pandas import DataFrame
np.set_printoptions(suppress=True, formatter={'float': '{:0.3f}'.format})
data = pd.read_table('res.txt', skiprows=[0, 2, 3], header=None, delim_whitespace=True,  error_bad_lines=False)
f1 = DataFrame(data)
s1 = np.array(f1)
length = s1[0, 2:5]
q = s1[0, 5:]
angle = [radians(q[0]), radians(q[1]), radians(q[2])]
k1 = [length[0], 0, 0]
k2 = [length[1]*cos(angle[2]), length[1]*sin(angle[2]), 0]
k3 = [length[2]*cos(angle[1]), length[2]*(cos(angle[0])-cos(angle[1])*cos(angle[2])/sin(angle[2])), length[2]*(sqrt(1 + 2*cos(angle[0])*cos(angle[1])*cos(angle[2])-(cos(angle[0]))**2-(cos(angle[1]))**2-(cos(angle[2]))**2)/sin(angle[2]))]
k = np.array([k1, k2, k3])
Aname = pd.read_table('res.txt', skiprows=range(0, 3)+range(4, 11), header=None, delim_whitespace=True)
temp = np.array(Aname)
h1 = temp[0, 1:]
atoms = s1[1:, 0]
number = (Counter([i[0] for i in atoms])).values()
vector = s1[1:, 2:5]
with open('POSC_.txt', 'w') as f:
    f.write("System ")
    f.write(str(h1)+'\n')
    f.write(str(k))
    f.write('\n'*2)
    f.write(str(number))
    f.write('\n'+'direct'+'\n')
    f.write(str(vector))
with open('POSC_.txt', 'r') as fpr:
    content = fpr.read()
content = content.replace('[', '')
content = content.replace(']', '')
content = content.replace(',', '')
content = content.replace("'", '')
with open('POSC_.txt', 'w') as fpw:
    fpw.write(content)
