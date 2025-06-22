#one line if
gender="M"
if gender=="M":
    print("male")
else:
    print("female")

print("Male") if gender=="M" else "Female"


#Datatype
#List
#they are separated by commas and encolsed in square bracket

a=[1,2,3,4,5,"Jenish"]
b=[] #it is empty list
print(type(a))
#positive index starts with 0 
#negative index starts with -1
print(a[0:5])  #---slicing highly used in machine learning
print(a[0],a[5])
print(a[-1],[-2])
print(len(a))
print(a[:])


#List method
#append==it adds data at last of the list and can add only one data at a time
# a.append(10)
# a.append("testing")
n=input("enter a word to add on list:")
print(a.append(n))


#insert
a.insert(1,"Bohara")
print(a)



d=[1,2,3,4,"Jenish","Bohara"]
d.insert(2,"gwak")
print(d)


#extend
data1=[1,2,3,4,5,6]
data2=[7,8,9,10,11,12,13]
data2.extend(data1)
print(data2)


# concat
data1=[1,2,3,4,5,6]
data2=[7,8,9,10,11,12,13]
data3=data1+data2
print(data3)
data2.extend(data3)
print(data2)
data2.insert(6,("cosmic"))
print(data2)


#data remove
#del
data1=[1,2,3,4,5,6]
data2=[7,8,9,10,11,12,13]















print(data2)
#clear
data2.clear()
print(data2)






# datatype
# list


# example
a = [1,2,2,3,"testing"]
print(type(a))
# pos index => start with 0
# neg index => start with -1
print(a[0],a[4])
print(a[-1],a[-2])


print(len(a))


a = [1,2,3,4,5,6,7,8,9,10]
print(a[1:4])
print(a[:4])
print(a[2:])
print(a[:])


a.append(10)
a.append("testing")
# n = input("Enter a word to add in list: ")
# a.append(n)


# insert

a.insert(234567,"indexone")

print(a)

# extends
data1 = [1,2,3,4,5]
data2 = [6,7,8,9,10,11,12,13]
data2.extend(data1)
print("extends",data2)
# a = [1,2,3,[1,2,3],[[1,1,3,5,[32,2,4,5]]]]

# concat
data1 = [1,2,3,4,5]
data2 = [6,7,8,8,8,8,9,10,11,12,13]
data3 = data1+data2



# data remove
# del
del data2[1]
print(data2)


# remove
data2.remove(8)
print(data2)

# pop
data2.pop()
print(data2)


#clear
data2.clear()
print(data2) 



#count
data2 = [6,7,8,8,8,8,9,10,11,12,13]
print(data2.count(8))
print(data2.reverse)
