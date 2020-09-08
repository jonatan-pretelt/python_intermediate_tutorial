from collections import Counter, namedtuple, OrderedDict, defauldict, deque

a = 'aaaaabbbbccc'
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))  #this could be indexed

Point = namedtuple('Point', 'x,y')
pt = Point(1,-4)
print(pt)
print(pt.x)  # can access the fields.
print(pt.y)

#OrderedDict are just regular dictionary but remembers orders the items were inserted
#defaultdict will have a default value if the key has not been set.
de = defaultdict(int)  #give it an int as a default type
###################################################################################
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.pop()
d.popleft()
d.extendleft([4,5,6])
d.rotate(1)
d.rotate(-1)
###################################################################################
