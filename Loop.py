#jab hamay nahi pata loop kitni baar chalay indefinite loop lagao while is one of them

#for loop is used when the number of iterations is known, whereas execution is done in a while loop until the statement in the program is proved wrong

#While Loop
i=1
while (i <= 8):    
    i=i+1
    print(i)
    
#For Loop
for i in range(0,9):
    print(i)

#jab hum string kai uper iterate kartay hain toh har aik character per iterate hoga , variable i ki assignment hogi and then print hoga 
name="Yusra"
for i in name:
    print(i)

#Range start hogi from 0 sai length of the name - 1 tak
name = "Yusra"
for i in range(len(name)):
    print(name[i])

#Given List of Numbers , Count Positive Intgers
numbers=[9,8,-8,6,7,-5,6]
positive_count_number= 0
for i in numbers:
    if i > 0:      
         positive_count_number = positive_count_number + 1        
print("The Number of Positive Numbers in a list are " , positive_count_number  )
#Humnai print statement ko for loop kai baahir rajha hai agar hum andar rakhtay toh yeh statement multiple times
#print hoti 

#Print a table of given number 5 skipping fifth iteration
#Continue statement is used to end current iteration and move towards the next iteration 
number=5
for i in range(1,11):
    if i == 5:
        continue
    print(number ," X " , i , "=" , number * i)

#Reverse a String using Loop
string="yusra"
reverse_string=""
for i in string:
    reverse_string=i + reverse_string
print(reverse_string)

#Write a character that has occurence once in the string
#A count method returns a numeric value denoting the number of occurrences of an element in the given input list
Our_Input="teeter"
for i in Our_Input:
    if Our_Input.count(i) == 1:
        print(i , "is the Character that has occurence one")

#Find factorial using while loop
number=5
factorial=1
while (number > 0):
    factorial=factorial*number
    number=number-1
print(factorial)

#Keep asking user for input untill they enter number between 5 and 9
#While true sai infinite loop lag gaya jab tak condtion meet nahi hojaati
while True:
    a=int(input("Enter Number"))
    if 5 <= a <= 9:
        print(a)
        break
    else:
        print("Invalid Try Again")
    
#Check if the number is prime 
number = 7
is_prime = True
if number <= 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

print(is_prime)

#Print Natural Numbers 
n=1
while (n <= 11):
    print(n)
    n=n+1

#Write a cube root
a=int(input("Enter Number: "))
for i in range(1,a+1):
    cube=i*i*i
    print(" The Cube of " , i ,"is" , cube)
#what you did wrong was kai you wrote for i in a which is not possible since it is an integer

# Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
reverse_list=reversed(list1)
for i in reverse_list:
    print(i)
list1 = [10, 20, 30, 40, 50]
size=len(list1)
for i in range(size-1 , -1 , -1):
    print(list1[i])
#size-1 means index should be 4 -1 means index 0 per stop karay gaa 

for i in range(-11,0,1):
    print(i)