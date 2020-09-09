# def mygenerator():
#     yield 1
#     yield 2
#     yield 3

# g = mygenerator()

# # for i in g:
# #     print(i)

# # value = next(g)
# # print(value)

# # value = next(g)
# # print(value)

# # value = next(g)
# # print(value)

# # print(sum(g))
# print(sorted(g))

#This method takes a lot of memory
def firstn(n):
    nums = []
    num= 0
    while num < n:
        nums.append(num)
        num +=1
    return nums

# print(firstn(10))
###################################

#This is a gnerator and is more efficient
import sys
def firstn_generator(n):
    num = 0
    while num <n:
        yield num
        num += 1

print(sum(firstn(10)))
print(sum(firstn_generator(10)))


print(sys.getsizeof(firstn(1000000)))          #returns size in bytes
print(sys.getsizeof(firstn_generator(1000000)))


def fibonacci(limit):
    print('start of fibonacci series')
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
    print('end of fibonacci series')

fib = fibonacci(30)


for i in fib:
    print(i)


mygenerator = (i for i in range(10) if i%2==0)
for i in mygenerator:
    print(i)

