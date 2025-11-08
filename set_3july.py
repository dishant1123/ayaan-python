# set : mutable , unique collection  , unordered 

"""
s1={1,2,3,4,5,6,"ayyan,",4j,66,77,77,6}
print(s1)
print(type(s1))
"""

# empty  set : 

"""s1 =set()
print(s1)
print(type(s1))
"""

# built-in  function : len  min max sorted sum 

"""
s1 ={1,2,3,4,5,55,6,7,89,0}
print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))
print(sum(s1))
"""
# slicing  : not  possible
"""
s1 ={1,2,3,4,5,55,6,7,89,0}
print(s1[8])
"""
# method : 

# s1 ={1,2,3,4,5,55,6,7,89,0}

"""s1.add(100)
print(s1)
s1.add(100)
print(s1)
"""
"""s1.clear()
print(s1)"""

"""s2 = s1.copy()
print(s2)"""
"""s2={55,0,33}
s1.update(s2)
print(s1)
"""

"""
s1.discard(55)
print(s1)

s1.remove(0)
print(s1)
"""
"""s1.pop()
print(s1)"""

# s1= {1,2,3,4}
# s2={2,4,6}
# s3={1,2,3,4,5,6,7,8,9,10}

"""print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
"""
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))
# s1.symmetric_difference_update(s2)
# print(s1)

# print(s1.intersection(s2))
# s1.intersection_update(s2)
# print(s1)

# s1= {1,2,3,4}
# s2={2,3,4}
# s3={1,2,3,4,5,6,7,8,9,10}

"""print(s1.isdisjoint(s2))
print(s3.issuperset(s1))
print(s2.issubset(s1))
"""

# frozenset : immutable set 

s2 =frozenset({1,2,3,4,5,6})
print(s2)
print(type(s2))

