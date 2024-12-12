import pandas as pd
import numpy as np

# pd.__version__
# pd.show_versions()

# 1

series = pd.Series(dtype=float)
print(series)

# 2

x=[1,2,3,4,5,6]
y= pd.Series(x)
print(y)

# 3

y.name = 'My letters'
print(y)
print(y.values)

#5

y.index = ['one', 'two', 'three', 'four', 'five','six']
print(y)

#6

print(y.iloc[0])
# 7
print(y.iloc[-1])

#8

print(y.iloc[1:5])

#9

print(y.iloc[::-1])

#10

print(y.iloc[[0,-1]])

# 11

print(y.astype(float))

#12

print(y[::-1])

# 13

print('sort****')
print(y.sort_values())
# 14
y.iloc[5] = 10
# 5 nes pas mane 6 skaiciai o ne 5

print(y)

# 15

y.iloc[1:5] = 0
print(y)

# 16

ay = y+5
print(ay)

#17 18

sr = pd.Series([-2,-1,0,1,2,5,6,10,10,2])
print(sr.loc[sr < 0])

# 19

print(sr>=5)

#20

print(sr>sr.mean())

# 21

x=pd.Series([-2, -1, 0, 1, 2, 5, 6, 10, 10, 2])

ex = x[x.isin([2,10])]
print(ex)

# 22
res = (x!=0).all()
print(res)

# 23

res = (x==0).any()
print(res)

# 24

print(x.sum())

#25

s = pd.Series([1,2,3])
print(s.mean())
