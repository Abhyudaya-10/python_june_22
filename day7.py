a=[1,2,3,4,5,["hello","jenish","world"]]
print(len(a))
print(a[-1])
b=a[-1]
print(b[0],b[2])



#wap to take 5 input from users add all items in list and print last item of list
a=[]
val1=input("1st item:")
val2=input("2nd item:")
val3=input("3rd item:")
val4=input("4th item:")
val5=input("5th item:")
b=val1,val2,val3,val4,val5

a.extend(b)
print(a)
print(a[-1])




