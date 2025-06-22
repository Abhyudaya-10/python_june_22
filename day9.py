# tuple
a=(1,2,3,4,5)
data=list(a)
print(a)


#set doesnt store duplicate data
a={"Jenish",1,2}
a={1,1,1,1,2,"Jenish"}
print(a)

data1=[1,1,1,1,2,2,2,3,4,5]
data2=set(data1)
print(data2)
data1=list(data2)
print(data1)
data1.remove(3)
print(data1)
