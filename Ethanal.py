import pandas as pd
import numpy as np
lines = open(r'ethanal.mol').readlines()
Nlist = [[],[],[]]
Dict = dict()
c = 1

for line in lines:
    if len(line.split()) == 7:
        Nlist[0].append(int(line.split()[0]))
        Nlist[1].append(int(line.split()[1]))
        Nlist[2].append(int(line.split()[2]))
    if len(line.split()) == 16:
        Dict[c] = line.split()[3]
        c += 1

df1 = pd.DataFrame(
        {'Atom1' : Nlist[0],
         'Atom2' :  Nlist[1],
         'Bonds' : Nlist[2],
         }
     )
df2 = pd.DataFrame(
        {'Atom1' : Nlist[1],
         'Atom2' :  Nlist[0],
         'Bonds' : Nlist[2],
         }
     )
     
df = pd.concat([df1, df2])
I = df.groupby(['Atom1']).sum()

for i in I['Bonds'].index:
    print 'Degree of nodes for element %s is %d'%(Dict[I['Bonds'].index[i-np.min([I.index])]] , I['Bonds'][I['Bonds'].index[i-np.min([I.index])]])