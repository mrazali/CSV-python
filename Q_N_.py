## Author : Muhammad Raza Ali
## Mail   : muhammadrazaali.raza@gmail.com



######## Finding the hightest Value from Column Q
max_20 = {}
N_column = dt['Horse']
Q_column = dt['MPS']          

for i in range(0,891):
    max_20[Q_column[i]] = N_column[i]

import itertools  
out = dict(itertools.islice(max_20.items(), 20))  
print(out)  # output the Number of Column Q
################
