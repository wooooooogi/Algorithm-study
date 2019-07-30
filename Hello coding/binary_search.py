# -*- coding: utf-8 -*-

#   coded by Sungwook Kim
#   Date: 2019-07-30
#   IDE: Spyder 3
#   Python version: 3.6.5

'''
Search: Figure out which is same as input in array. (or bunch of things)
Method(or way, manner, means) 1: Search from the beginning.
Method 2: Binary search, search from middle for all time.
'''
import time
import random
search_area = 10000000
search_num = int(random.random() * search_area)
arr = range(search_area)
print("Search area: {search_area}, Search number: {search_num}".format(search_area=search_area, search_num=search_num))
'''
Method 1: Search from the beginning. (Simple search) O(n)
'''
start_time = time.time()
#print(start_time)
for i in range(search_area):
    if search_num == arr[i]:
        print("Search complete, search_num is {search_num}".format(search_num=search_num))
        break
end_time_1 = time.time() - start_time
print(end_time_1)

'''
Method 2: Search from the middle. (Binary search) O(log_2_n)

Try 1.
start_time = time.time()
k = int(search_area / 2)
while True:
    print(k)
    time.sleep(0.1)
    if search_num == arr[k]:
        print("Search complete, search_num is {search_num}".format(search_num=search_num))
        break
    elif search_num > arr[k]:
        k = int(search_num - k / 2)
    else:
        k = int((search_num - k) / 2)
end_time_2 = time.time() - start_time
print(end_time_2)

Try 2.
'''
start_time = time.time()
k = int(search_area / 2)
k0 = search_area
k1 = 0
while True:
    if search_num == arr[int(k)]:
        print("Search complete, search_num is {search_num}".format(search_num=search_num))
        break
    elif search_num > arr[int(k)]:
        k1 = (k)
        k = ((k0 - k) / 2 + k)
    else:
        k0 = (k)
        k = ((k - k1) / 2 + k1)
end_time_2 = time.time() - start_time
print(end_time_2)

'''
Compare algorithms
'''
print("Search area: {search_area}, Search number: {search_num}".format(search_area=search_area, search_num=search_num))
#print("Method 1: {time1}, Method 2: {time2:.10f}, Method1/Method2 = {timeDiv}".format(time1=end_time_1, time2=end_time_2, timeDiv=end_time_1/end_time_2))
#   Since Method2's takt time is too short. Div by 0 error occurs.
