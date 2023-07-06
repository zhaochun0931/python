import re

txt = "age=10,no=11,score=100"
xx = re.findall("\d+",txt)
print(xx)

# ['10', '11', '100']



for i in xx:
    print(i)



# 10
# 11
# 100






txt = "hello this is a demo test"

xx = re.findall('is.',txt)
print(xx)
# ['is ', 'is ']


xx = re.findall('is.*',txt)
print(xx)
# ['is is a demo test']

xx = re.findall("is.*?",txt)
print(xx)
# ['is', 'is']
