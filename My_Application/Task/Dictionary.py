
fruits={}
count=0
fruits_count=int(input("How many fruits you want to add? "))
for i in range(fruits_count):
    count+=1
    print("********************")
    print("Fruit: ",count)
    print("********************")
    name=input("Enter name of fruit:")
    color=input("Enter color of fruit:")
    fruits[name]=color
    
print("------------------------------")
print("Fruits name with color")
print("------------------------------")
for key,value in fruits.items():
    print(key,":",value)
    