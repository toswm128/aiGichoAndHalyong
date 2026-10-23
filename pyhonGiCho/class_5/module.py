import math
import random as r
import statistics as st


print('log', math.log(8, 2))
print('pi', math.pi)
arr = [i for i in range(99)]
arr.append(100)
print('sample', r.sample(arr, 10))
print('ramdom float', r.random())
print('ramdom int', r.randint(1, 10))
print('choice', r.choice(arr))
print('mean', st.mean(arr))
print('median', st.median(arr))
print('variance', st.variance(arr))
print('stdev', st.stdev(arr))
