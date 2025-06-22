#Dictionary
#dict
userinfo={
    "name":"Jenish",
    "age":17,
    "religion":"Hindu"
}
print(type(userinfo))
print((userinfo["name"]))#to access data in dictionary
print(type(userinfo["age"]))


userinfo["age"]=69
print(userinfo)
userinfo["address"]="Thimi"
print(userinfo)

userinfo2={
    "phone":9806696969,
     "perm address":"dadeldhura"
}
userinfo2.update(userinfo)
print(userinfo2)
print(userinfo2.get("age"))

#removing mehod from dictionary
test = {
    "name":"broadway",
    "greet":"hello",

}
# del test["greet"]
# print(test)

# test.pop("name")
# print(test)

test.popitem()#deletes last item of th dict
print(test)





user = {
    "name":"Sudan",
    "phone":[98062, 98449]
}

# phone number is 98062
# phone number is 98449

a=user.get("phone")

print("phone numer is",a[0])
print("phone numer is",a[1])


user = {
     "name":"Sudan",
     "phone":[
         {
             "type":"Ntc",
             "number":"98449"
         },
         {
             "type":"Ncell",
             "number":"98062"
         }
     ]
 }

# Ntc number is 98449
# Ncell number is 98062
phone=user.get("phone")
print(phone)
phone1=phone[0]
phone2=phone[1]
print(f"Ntc number is {user['phone'][0]['number']}")
