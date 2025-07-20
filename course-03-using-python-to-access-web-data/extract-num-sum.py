import re
file = open('D:/Learning/Python for Everybody Coursera/Course 3/regex_sum_2250165.txt')
numlist = list()
for line in file:
    line = line.rstrip()
    nums = re.findall('[0-9]+',line)
    for num in nums:
        numlist.append(int(num))
sum = sum(numlist)
print('Sum: ',sum)

