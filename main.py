directoryName = input("Enter directory Name: ")
file_name = input("Enter file Name: ")
user_name = input("Enter your full Name: ")
address = input("Enter your address: ")
phone_number = input("Enter your phone number: ")
line = user_name+", "+address+", "+phone_number

f = open(file_name, "x")
f.write(line)
f.close()
print(line)