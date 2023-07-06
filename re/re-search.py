import re


txt = "hello this is a demo test"
xx = re.search('this',txt)
print(xx)

# <re.Match object; span=(6, 10), match='this'>



print("start index:",xx.start())
print("end index:",xx.end())


# start index: 6
# end index: 10








xx = re.match('hello',txt)
print(xx)

# <re.Match object; span=(0, 5), match='hello'>

xx =  re.match('this',txt)
print(xx)

# None


xx = re.search('this',txt)
print(xx)

# <re.Match object; span=(6, 10), match='this'>
