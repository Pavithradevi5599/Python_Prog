i=0
while(i==0):
    data=input("Enter your data:")
    length=len(data)
    if(length<5):
        print("Your data length should be greater than 5")
    elif(length>=5):
        print("*****************************")
        print("Your entered data:",data)
        print("Length of data:",length)
        print("*****************************")
        i=1
       
def count_letters(data):
    #empty dictionary used to store the counts of each letter
    letter_counts = {}
    for char in data:
        if char.isalpha():
            char = char.lower() 
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts
letter_counts = count_letters(data)
for letter, count in sorted(letter_counts.items()):
    print(f"{letter}: {count}")
    


