#lambda arguments: expression

add10 = lambda x: x +10

print(add10(5))


mult = lambda x,y: x*y

print(mult(2,7))

#map(func,seq)
a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x*2, a)
print(list(b))

#list comprehension
c = [x*2 for x in a]
print(c)

#filter(fun, seq)
d = filter(lambda x: x%2==0, a)
print(list(d))

#list comprehension
e = [x for x in a if x%2==0]
print(e)

#reduce(func, seq)
from functools import reduce

product_a = reduce(lambda x,y: x*y, a)
print(product_a)

