#sets define inf flower braces {}
#no indexing
a={'a','sita', 'ram', 'lakshman', 'hanuman', 'jaya', 'Rama', 'Krishna'}
print(a)
print(len(a))
b={1,'a',True}#1,TRUE understands as the same so True is ignored
print(b)
c={True,'a',1}
print(c)
a.add('f')
print(a)
print(a.pop())
a.update(b)
print(a)
#it will consider only unique values when we update with other sets
#del(a)
a.clear()
print(a)
# a.union(b)
# a.intersection(b)
# a.difference(b)
# a.symmetric_difference(b)
# a.isdisjoint(b) return boolean values
# a.issubset(b)
# a.issuperset(b)