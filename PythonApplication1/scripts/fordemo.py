for a in [3,4.4,'life']:
    print a
    
idx=range(5)
print idx


for a in range(10):
    print a**2

i=1
while i<10:
    print i
    i=i+1
    
def square_sum(a,b):
    c=a**2+b**2
    return c

print square_sum(3,4)



a=1
def change_integer(a):
    a=a+1
    return a
print change_integer(a)
print a


b=[1,2,3]
def change_list(b):
    b[0]=b[0]+1
    return b
print change_list(b)
print b
