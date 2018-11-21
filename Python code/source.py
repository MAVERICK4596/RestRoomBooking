from core_function import Find_the_next
from core_function import check_the_emp
import json 
print("Welcome to RestoBook Service ")
print("Please enter your emloyee number as '1 employeenumber' if you are booking and '0 employee number if you are leaving :-) ")
print("  ")

with open("./data.json", "r") as fp:
    data = json.loads(fp.read())

list_src=data["list"]
input_string=input("Please provide the employee nummber:")

if (input_string[0]=="1"):
    if(check_the_emp(input_string[2:])):
       print("A booking already exists for the Employee:{}".format(input_string[2:]))
    else:
        index_number = Find_the_next(list_src)
        data["list"][index_number]=1
        data["employee"][input_string[2:]]=index_number
        with open("./data.json", "w") as fp:
            json.dump(data, fp)
        print("Restroom NO {} has been booked by the employee with id:{}".format(index_number+1,input_string[2:]))
elif(input_string[0] == "0"):
    if(check_the_emp(input_string[2:])):

        index_number = data["employee"][input_string[2:]]
        data["list"][index_number]=0
        with open("./data.json", "w") as fp:
            json.dump(data, fp)
        print("Restroom NO {} is free to occupy now".format(index_number))

    else:
        print("No booking exists from the Employee:{}".format(input_string[2:0]))

else:
    print("Please go through instructions provided.")
