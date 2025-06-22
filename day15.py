#keyword arguments
# def user_info(Name,Role):
#     print("Name is:",Name)
#     print("Role is:",Role)
#     return()
# user_info(Role="Student",Name="Jenish")

# def calculate_discount(price,discount=10):
#     print("The price of goods is:",price)
#     print("Discount on goods is:",discount)
#     if price<=150:
#         discount_price=price-10/100
#         return(discount_price)
#     else:
#         discount_price=price-15/100
#         return(discount_price)
# print("Price after discount:",calculate_discount(price=140))
# print("Price after discount:",calculate_discount(price=350,discount=15))



def result(data={
    "name":"Jenish",
    "total":560,
    "count":6
}):
    Name=data.get("name")
    
    Marks_total=data.get('total')
    
    Subject_count=data.get('count')
    
    Jenish_percentage=Marks_total/Subject_count
    return(Jenish_percentage)

print("The percentage of:",result())


def sum_dict(sum = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40,
    "e": 50,
    "f": 60,
    "g": 70,
    "h": 80,
    "i": 90,
    "j": 100
}):
    a=sum['a']
    b=sum['b']
    c=sum['c']
    d=sum['d']
    e=sum['e']
    f=sum['f']
    g=sum['g']
    h=sum['h']
    i=sum['i']
    j=sum['j']
    add=a+b+c+d+e+f+g+h+i+j
    return(add)
print("The sum of:",sum_dict())


def sum_dict(sum = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40,
    "e": 50,
    "f": 60,
    "g": 70,
    "h": 80,
    "i": 90,
    "j": 100
}):
    value=sum.values()
    return(value)
print(sum_dict())
