for i in range(1,4):
    for j in range(1,4):
        print(j)
    print()

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j}:{i*j}")
    print()

# Print the following:
# *
# * *
# * * *
# * * * *

for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=' ')
    print()

# Print:
# * * * *
# * * *
# * *
# *

for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()



#     Print a 4x4 grid like:
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
for i in range(1,5):
    for j in range(1,5):
        print(j,end=" ")
    print()

# Print:
#    *
#   * *
#  * * *
# * * * *
 
d=[10,50,3,5,6,7,8]
for i in d:
    for j in range(1,11):
        print(f"{i} x {j}:{i*j}")
    print()


data=[10,2,6,4,5,11,11,11,45]
data=set(data)
data=list(data)
print(data)
for i in data:
    for j in range(1,11):
        print(f"{i} x {j}:{i*j}")
    print()

a=[1,2,3,4,None,None]
final=[]
for i in a:
    if i is None:
        continue
    final.append(i)
print(final)



a=[1,2,3,"test",4.0,2.8,"testing world"]
final=[]
for i in a:
    if isinstance(i,int) or isinstance(i,float):
        final.append(i)
print(final)