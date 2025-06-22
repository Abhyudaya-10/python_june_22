#  function
def add_func():
    print(1+2)
    return
add_func()


def test_func():
    print("I am Jose Mourinho")
    return()
test_func()
def sum():
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    sum=a+b
    print(sum)
    return()
print(sum())


#positional arguments
def user_info(name,role):
    print("name:",name)
    print("role:",role)
    return()


user_info("Jenish","students")


def shoppingcart_func(price,quantity):
    total=price*quantity
    print("Total is:",total)
    return()
price=int(input("enter the price:"))
quantity=int(input("enter the quantity:"))
shoppingcart_func(price,quantity)


# qno.1  Create a function that takes three integers and returns the second largest number among them. All three integers should be passed as positional arguments.
def integers_func(int1,int2,int3):
    if(int1>int2 and int1>int3):
        return(int1)
    elif(int2>int1 and int2>int3):
        return(int2)
    else:
        return(int3)
int1=int(input("enter a number:"))
int2=int(input("enter a number:"))
int3=int(input("enter a number:"))
print("The largest number is",integers_func(int1,int2,int3))


def lists_func(a, b):
    result = []
    for i in a:
        if i in b:
            result.append(i)
    return(list(set(result)))


print(lists_func([1, 2, 3, 3, 3, 4, 3],[1, 2, 6, 8, 4, 3]))



#HOMEWORK
# Define a function that accepts four parameters: length, width, height, and unit_price. It should calculate the cost to fill a box (volume × unit_price) using positional arguments only. Then call the function with appropriate values.
def dimension(length,width,height,unit_price):
    volume=length*width*height
    cost=volume*unit_price
    return(cost)
print("The dimensions are:",dimension(5,3,4,10))

# Create a function that takes a base and an exponent (both integers) and returns the power (i.e., base raised to the exponent). Use only positional arguments.
def math(base,exponent):
    power=base**exponent
    return(power)
print("power:",math(7,4))


# Define a function that takes three sides of a triangle and returns whether the triangle is valid or not (based on triangle inequality). All arguments must be positional.
def triangle(a,b,c):
    if a+b>c and a+c>b and b+c>a :
        return(a+b>c and a+c>b and b+c>a)
print("Validity of Triangle:",triangle(3,4,5))


# Write a function that takes two tuples of the same length and returns a new tuple where each element is the sum of elements from both tuples at the same index
def tuples(tup1,tup2):
    new=()
    if len(tup1)==len(tup2):
        return(tup1+tup2)
print("New elements:",tuples((1,2,3),(4,7,2)))

'''
Write a function that takes the radius of a circle and returns the area of the circle using the formula 
𝜋
𝑟  
2
πr 
2
 . Use only positional arguments.
'''
def circle_area(𝜋,radius):
    area=𝜋*radius**2
    return(area)
print("The area of the circle:",circle_area(3.14,6))