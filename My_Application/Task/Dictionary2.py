User={}
count=0
user_count=int(input("How many users you want to add? "))
for i in range(user_count):
    count+=1
    print("********************")
    print("User: ",count)
    print("********************")
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    city=input("Enter your city:")
    mobile=input("Enter your mobile:")
    salary=input("Enter your salary:")
    User[name]=salary
    print("------------------------------")
    print("User details\n")
    print("*******************")
    print("NAME\tSALARY")
    print("*******************")
    for key,value in User.items():
        print(key,"\t",value)
    print("*******************")

"""
i=0
while(i==0):
    print("1.Age\n2.City\n3.Mobile\n4.Salary\n5.All\n6.Exit")
    print("------------------------------")
    choice=int(input("Select which one you want to see:"))
    if(choice==1):
        User[name]=name
    elif(choice==2):
        User[name]=city
    elif(choice==3):
        User[name]=mobile
    elif(choice==4):
        User[name]=salary
    elif(choice==5):
        User[name]=age,city,mobile,salary
    elif(choice==6):
        exit()
        i=1
    else:
        print("Invalid input!!!!")
"""
    