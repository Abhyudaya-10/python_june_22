# # break and continue
# a=[1,2,3,4]
# for i in a:
#     if i==3:
#       break
#     print(i)



a=[1,2,3,"test",4.0,2.8,"testing world"]
result=[]
for i in a:
    if isinstance(a,int) or isinstance(a,float):
        result.append(i)
print(result)


















a=[1,2,2,2,None,None,"jenish",None]






















#nested for loop
d=[10,50,3,5,6,7,8]
for i in d:
    for j in range(1,11,1):
        print(f"{i} x {j}={i*j}")
    print("\n")



data=[10,2,6,4,5,11,11,11,45]
data1=set(data)
print(data1)
data=list(data1)
print(data)
for i in data:
    for j in range(1,11,1):
        print(f"{i} x {j}={i*j}")
    print("\n")


a=[1,2,3,4,None,None]
final=[]
for i in a:
    if i is None:
        continue
    final.append(i)
print(final)
