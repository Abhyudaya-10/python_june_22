a = [1,2,3,4,5,6]



# in ,
# not in
print(7 not in a)


# Loops

for i in [1,2,3,5,6,7]:
    print(i)
for i in ["broadway","education","nepal"]:
    print(i)

for i in range(1,10,1):
    print(i)

# range(1,10) => by default step or increament value is 1
# range(10) => by default start value is 0 and increament value is 1

for i in range(10):
    print(i)
'''


2 X 1 = 2
.....
2 X 10 = 20

'''


print(f'2 X 1 = {2*1}')
print(f'2 X 2 = {2*2}')
print(f'2 X 3 = {2*3}')
print(f'2 X 4 = {2*4}')
print(f'2 X 5 = {2*5}')
print(f'2 X 6 = {2*6}')
print(f'2 X 7 = {2*7}')
print(f'2 X 8 = {2*8}')

print("......................")


for i in range(1,11,1):
    print(f'2 X i = {2*i}')




people = [
    {"name":"sudan","dob":"06-18"},
    {
        "name":"Madan",
        "dob":"01-06"
    },
    {
        "name":"suman",
        "dob":"01-06"
    },
    {
        "name":"sameep",
        "dob":"03-10"
    },
]

current_date = "03-10"
for i in people:
    if current_date == i['dob']:
        print(f"Happy birthday, {i['name']}")



user = {
    "name":"Sudan",
    "phone":[
        {
            "type":"Ntc",
            "number":"98449"
        },
        {
            "type":"Hello Nepal",
            "number":"98162"
        },
        
    ]
}

# Ntc number is 98449
# Ncell number is 98062
phone = user.get('phone')
for i in phone:
    print(f"{i['type']} number is {i['number']} ")