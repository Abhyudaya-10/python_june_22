#Given a nested dictionary representing student data (e.g., names as keys and another dict of subject:marks), how would you extract all students who scored more than 80 in Math?
student_data = {
 "Jenish":
     {
        "maths":80,
        "physics":90
     }
    ,
    "Anubhav":
        {
        "maths":50,
        "physics":70
        }
    ,
    "Mantra":
        {
        "maths":85,
        "physics":89
        }
    ,
}
if student_data ["Jenish"]["maths"]> 80:
    print('Jenish')
if student_data ["Anubhav"]["maths"]> 80:
    print('Anubhav')
if student_data ["Mantra"]["maths"]> 80:
    print('Mantra')


# Give two dictionaries with overlapping keys, how would you combine them by summing the values of common keys?
dict1={
    "a":1,
    "b":2,
    "c":3
}
dict2={
    "b":4,
    "c":5,
    "d":6
}
x=dict1.get("a")
y=dict1.get("b")
z=dict1.get("c")






for i in range(50,100):
    if i%2==0:
        print(i)
