

import csv
import numpy as np

# import the csv data of B2 gaps generated fsolve

csvSource = open('B2gaps_32bar096Tc.csv','r')
B2gaps = list(csv.reader(csvSource, delimiter=','))
csvSource.close()

# print(data)


list_all = list(zip(*B2gaps))
# print(list(list_all[2]))

hList = []
for ii in list(list_all[2]):
    hList.append(float(ii))

hArray = np.array(hList)    

# print(hList)    
    
DuuList = []
DddList = []
DudList = []

for ii in list(list_all[3]):
    DuuList.append(float(ii))    

for ii in list(list_all[4]):
    DddList.append(float(ii))    

for ii in list(list_all[5]):
    DudList.append(float(ii))    


# print(DudList)    

DuuArray = np.array(DuuList)
DddArray = np.array(DddList)
DudArray = np.array(DudList)
