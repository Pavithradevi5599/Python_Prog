def triangle_pattern(rows):
    space=rows-1
    for i in range(0,rows):
        for j in range(0,space):
            print(end=" ")
        space=space-1
        for j in range(0,i+1):
            print(str,"",end="")
        print("\r")
rows=int(input("Enter number of rows:"))
str=input("Enter any string:")
triangle_pattern(rows)
