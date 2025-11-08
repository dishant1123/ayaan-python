# list  :  mutable  ==>  changes in list  ==>  odered list

"""l1=[1,2,3,4,5,6,7,8,9,"ayyan",12.23,2j]
print(l1)
print(type(l1))
"""
# builtin function  :  len min max sorted sum 

"""l1=[10,2,3,4,5,6,7,8,9,12.23]
print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1))
print(sum(l1))
"""
# slicing  : 
# pos index : 0 1 2 .....  l to r 
# neg  index : -1 -2 ..... r to l

l1=[10, 2, 3, 4, 5, 6, 7, 8, 9, 12.23]
#   0  1   2  3  4  5  6  7  8  9 
"""
print(l1[0])
print(l1[9])

"""
# l1[0]=100  # changes in list 
# print(l1)
"""
print(l1[0 : 3])   # 0 starting index 3  ending  index 
print(l1[ : 5])
print(l1[2: ])

print(l1[2 : 6 : 2])  # 2start index 6  ending index 2  step size 
print(l1[ : : 2])
print(l1[ : : -2])
print(l1[ : : -1])
"""

# method  : 
l1=[10, 2, 3, 4, 5, 6, 7, 8, 9, 12.23,10]

# l1.append(150)
# print(l1)

# l1.clear()
# print(l1)

# l2 = l1.copy()
# print(l2)

"""l2=["banana","apple","mango","orange","grapes","banana"]

l1.extend(l2)
print(l1)
"""

"""l1.insert(3,250)
print(l1)
"""

"""print(l1.index(12.23))
print(l1.index(10))
print(l1.index(10,1,11))
"""

"""l1.pop(5) # remove  from index numwise 
print(l1)

l1.remove(12.23)
print(l1)"""

l1.reverse()
print(l1)

l1.sort()
print(l1)