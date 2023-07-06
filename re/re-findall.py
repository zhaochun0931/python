import re

xx = re.findall("\d+","age=10,no=11,score=100")
print(xx)

# ['10', '11', '100']



for i in xx:
    print(i)



# 10
# 11
# 100
