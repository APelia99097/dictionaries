people = [
    {'first_name': "Bob", 'last_name': "Singh", 'phone_number': "604-983-1723"},
    {'first_name': "Billy", 'last_name': "Singh", 'phone_number': "604-573-9269"},
    {'first_name': "Jone", 'last_name': "Singh", 'phone_number': "604-583-9491"}
]


for person in people:
    fname = person['first_name']
    lname = person['last_name']
    pnumber = person['phone_number']

    print("Information")
    print(f" {lname}, {fname}'s phone number is {pnumber}")