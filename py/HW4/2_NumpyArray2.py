from timeit import default_timer as timer
from numpy import *
# 比較三種方法
# 法一
start = timer()
for x in range(100):
 j = []
 for i in range(10000): 
     j.append(i**2)
end = timer()
print(end-start) # 秀出執行時間

# 法二
start = timer()
for x in range(100): 
    j=[i**2 for j in range(10000)]
end = timer()
print(end-start) # 秀出執行時間

# 法三
start = timer()
for x in range(100):
    j=arange(10000)**2
end = timer()
print(end-start) # 秀出執行時間