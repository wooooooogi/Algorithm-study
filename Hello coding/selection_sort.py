#   Coded by Sungwook Kim
#   Date: 2019-07-30
#   Python version: 3.6.5
#   IDE: Spyder 3

#   Sort, information = [Name, Date, E-mail]

#   Sample code is 2001 year's 메리츠화재 stock information. (Downloaded in KRX)

#   Sort by price (When is the highest price in 2001)

import pandas as pd
import numpy as np
import os
#   Use pandas library to get csv information.
Data = pd.read_csv(os.getcwd() + "/selection_sort_sample_code.csv", encoding="ms949", index_col=False)
print(Data)
Data = Data[:-1]
#print(Data)

sorting_variable = "종가"
sorted_variable = "년/월/일"

SV = Data[sorting_variable]
SV = [SV]
#SV = np.array()
#print(SV)
#for i in SV:
#    for j in SV:
#        if i < J:
#            break
    