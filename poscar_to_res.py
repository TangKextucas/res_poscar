import pandas as pd
from pandas import DataFrame
from math import*
import numpy as np
np.set_printoptions(suppress=True, formatter={'float': '{:0.5f}'.format})
pd.set_option('precision', 5)        							   #set precision
data = pd.read_table('CONTCAR', sep=' ')  					  #read it simply
f1 = DataFrame(data)
s1 = np.array(f1)
K = [0.0, 0.0, 0.0]
for i in range(0, 3):    									  #skipover Nan values
    K[i] = np.array([x for x in s1[i+1] if str(x) != 'nan'], dtype=float)
K = np.array(K)
f = lambda q: q*180/pi      								#transfer rad to angle
angle = [f(acos(np.vdot(K[0], K[1]))), f(acos(np.vdot(K[0], K[2]))), f(acos(np.vdot(K[1], K[2])))]
length = np.array([sqrt(np.vdot(K[0], K[0])), sqrt(np.vdot(K[1], K[1])), sqrt(np.vdot(K[2], K[2]))])
Aname = [x for x in s1[4] if str(x) != 'nan']
number = [x for x in s1[5] if str(x) != 'nan']
number = np.array(number, dtype=int)
g = sum(number)     										    #number of atoms
kh = []
for i in range(0, g):
    kh.append(0.0)
for i in range(0, g):
    kh[i] = [x for x in s1[i+g-1] if str(x) != 'nan']
kh = np.array(kh, dtype=float)
w1 = np.ones(g)
w2 = np.zeros(g)
kh = np.insert(kh, 3, values=w1, axis=1)  			#insert a column into Dataframe
kh = np.insert(kh, 4, values=w2, axis=1)
r1 = []
for i in range(0, 5):
    r1.append('%')
Atom = []
Atype = []
for k in range(0, len(Aname)):
    for i in range(0, number[k]):
        Atom.append(Aname[k])
        Atype.append(k+1)
for i in range(0, g):
    Atom[i] += str(i+1)
kh = DataFrame(kh, index=Atom, columns=r1, dtype=float)
kh.insert(0, '(', Atype, allow_duplicates=True)
e1 = 'CELL   0.0000   '
with open('temp.txt', 'w') as f:
    f.write('TITL C'+'\n')
    f.write(e1)
    f.write(str(length)+'  ')
    f.write(str(angle)+'\n')
    f.write('LATT -1'+'\n')
    f.write('SFAC  ')
    f.write(str(Aname)+'\n')
    f.write(str(kh)+'\n')
    f.write('END')
with open('temp.txt', 'r') as fpr:
    content = fpr.read()
    for i in ['[', ']', ',', "'", '%', '(']: 			#delete these in temp.txt
        content = content.replace(i, '')
with open('temp.txt', 'w') as fpw:
    fpw.write(content)
def delblankline(infile, outfile):  				 # Delete blanklines of infile
    infp = open(infile, "r")
    outfp = open(outfile, "w")
    lines = infp.readlines()
    for li in lines:
        if li.split():
            outfp.writelines(li)
    infp.close()
    outfp.close()
delblankline("temp.txt", "HAHA.txt")
