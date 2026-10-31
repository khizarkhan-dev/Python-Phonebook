def check_person(contacts,name):
   if name in contacts:
       print(contacts[name])
   else:
       print("info invalid")

print("CONTACT")
contact = input("Enter name:")
print(f'just a sec, {contact}') 
contacts = {
    'Ali' : {
    "name" : "Ali",
    "age" : "19",
    "number" : "123-456-789-0",
    "status" : "student" 
    } ,
    
   'khizar' : {
    "name" : "khizar",
    "age" : "17",
    "number" : "123-456-789-0",
    "status" : "student"    
   }
}
check_person(contacts,contact)
