from timeit import default_timer as timer

My_string='934 2469'

My_String2=My_string.replace("934", "2684")
# print(My_String2)

My_String2.split()
''.join(My_String2)


my_list = ['a']*1000000

#bad use of code
start = timer()
My_string = ''
for i in my_list:
    My_string += i
stop = timer()
# print(My_string)
print(stop-start)

#good use of code

start = timer()
My_string = ''.join(My_string)
# print(My_string)
stop = timer()
print(stop-start)




