## Author = Muhammad Raza Ali 
## Email = muhammadrazaali.raza@gmail.com

import pandas as pd
import datetime
dt  = pd.read_excel('2021-02-14_Sunshine Coast-1.xlsx')    #### Loading Data in 

N_column = dt['Horse']           # N-column
month_Periods = []               # Month column[A and U] 
B_column = dt['Venue']           # Column - B
dt['RaceNo'] = dt['RaceNo'].astype(int)
E_column = dt['RaceNo']          # Column - E
Q_column = dt['MPS']             # Column - Q
I_column = dt['LastTen']         # Column - I
F_column = dt['Distance']        # Column - F
J_column = dt['Barrier']         # Column - J
K_column = dt['Weight']          # Column - K
O_column = dt['Sectional']       # Column - O
T_column = dt['ShortName']       # Column - T
AA_column = dt['TrainersTrack']  # Column - AA
P_column = dt['Distance.1']      # Column - P
X_column = dt['Weight.1']        # Column - X


######## output the Name of Column N
print("Output the Name containing N-column")
print(N_column)   # output the Name of Column N
################





######## output of Column A & N, which is Contaning two different Date and getting month Periods
for i in range(0,892):
    end_date = datetime.datetime.date(dt['Date'][i])
    start_date = datetime.datetime.date(dt['Date.1'][i])
    num = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    month_Periods.append(num)

month_Periods.sort(reverse=True)
print("       ")
for i in range (0,21):
    print(month_Periods[i])  # Month period of each two dates
print("       ")
##################





######## outputting the Number of Column E
import numpy as np
print("Output the Number containing E-column")
ary = np.asarray(E_column)
ary[::-1].sort()
print("       ")
for i in range (0,21):
    print(ary[i])   # output the Number of Column E
print("       ")
################





######## Finding the hightest Value from Column Q
max_20 = {}
N_column = dt['Horse']
Q_column = dt['MPS']          

for i in range(0,891):
    max_20[Q_column[i]] = N_column[i]

import itertools  
out = dict(itertools.islice(max_20.items(), 20))  
print("       ")
print(out)  # output the Number of Column Q
print("       ")
################



######## output of Column I, x on most right side or second most right side 
col = []
for i in I_column:
    col.append(str(i))

X_containg = []
for i in col:
    leng = len(i)
    if i[leng-1]=='x' or i[leng-2]=='x' :
        X_containg.append(i)

I_column=X_containg
print("       ")
for i in range(0,21):
    print(X_containg[i])    # Containg X on last 2 digits

print("       ")
##################


######## outputting the Value between 800-1300 from Column F
value = []
for i in F_column:
    if i>=800 and i<=1300:
        value.append(i)

print("       ")
print("Output the Value between 800-1300 from Column F")
print(F_column)   # output Value between 800-1300 from Column F
print("       ")
################


######## Containing Lower Number (1,2,3,4,5) from Column J
value = []
for i in J_column:
    if i<=5 and i>=1:
        value.append(i)

value.sort(reverse=True)
print("Lower Number (1,2,3,4,5) from Column J")
from collections import Counter
cnt = Counter()

for size in value:
    cnt[size] +=1
print("       ")
print("Each number with how many times occure")
print(cnt.most_common())# Lower Number (1,2,3,4,5) from Column J
print("       ")
################


######## Value should be less or equal to 58 from Column K
value = []
K_column = dt['Weight']
for i in K_column:
    if i<=58:
        value.append(i)

cnt = Counter()

for size in value:
    cnt[size] +=1

print("       ")
print("left number from K-Column and right number is how many times occure")
print(cnt.most_common())  # Value should be less or equal to 58 from Column K
print("       ")
################


######## Value between 31.00-33.99 from Column O
value = []
for i in O_column:
    if i>=31.00 and i<=33.99:
        value.append(i)

cnt = Counter()

for size in value:
    cnt[size] +=1
print("       ")
print("left number from O-column and right number is how many times occure")
print(cnt.most_common())   # Value between 31.00-33.99 from Column O
print("       ")
################



######## output of Column T, ["G1","G2","G3","LISTED"]
col = []
for i in T_column:
    col.append(str(i))

a= ["G1","G2","G3","LISTED"]
containg = []
for i in col:
    if any(x in i for x in a):
        containg.append(i)

cnt = Counter()

for size in containg:
    cnt[size] +=1


print("       ")
if (cnt.most_common()):
    print("left number from T-column and right number is how many times occure")
    print(cnt.most_common())    # Containg ["G1","G2","G3","LISTED"]
else:
    print("There is no Found G1,G2,G3,LISTED")
print("       ")
##################




######## Column AA and Column B is Equal values
col = []
numb = []
for i in range(0,len(B_column)-1):
    if B_column[i]==AA_column[i]:
        col.append(i)
        numb.append(B_column[i])


equal = {}

for c in col:
    for n in numb:
        equal[c] = n
        break 

import itertools  
aab = dict(itertools.islice(equal.items(), 20)) 
print("       ")
print("Column AA and Column B is Equal Values")
print(aab)   # Column AA and Column B is Equal Values
print("       ")
################



######## Column P and Column F is Equal values
colmn = dt['Distance']
col= []
numb = []
for i in range(0,len(P_column)-1):
    if colmn[i]==P_column[i]:
        col.append(i)
        numb.append(P_column[i])


equal_Distance = {}

for c in col:
    for n in numb:
        equal_Distance[c] = n
        break 

aab = dict(itertools.islice(equal_Distance.items(), 20)) 
print("       ")
print("Column P and Column F is Equal values")
print(aab)   # Column P and Column F is Equal values
print("       ")
################


######## Column K and Column U with Low weighted
K_col = dt['Weight']
U_column = dt['Date.1']
col= []
numb = []
for i in range(0,len(P_column)-2):
    if K_col[i]<X_column[i]:
        col.append(i)
        numb.append(U_column[i])


Low_Weighted_Date = {}

for c in col:
    for n in numb:
        Low_Weighted_Date[c] = n
        break 

col.sort(reverse=True)
print("       ")
print("Column P and Column F is Equal values")
for i in range(0,21):
   print(col[i]," : ",Low_Weighted_Date[col[i]])   # Column K and Column U with Low weighted
print("       ")
################