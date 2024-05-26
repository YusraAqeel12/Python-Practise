#1. Write a Python program to print the following string in a specific format (see the output).
print("Twinkle Twinkle Little Star, \n \t How I wonder what you are! \n \t \t Up above the world so high,  \n \t \t Like a diamond in the sky. \n Twinkle, twinkle, little star,  \n \t 	How I wonder what you are " )

#Find Radius of circle
import math
radius = int(input("Enter Radius"))
output=3.14*(pow(radius,2))
print(output)

#Enter your name in reverse order 
FirstName=input("Enter First Name")
SecondName=input("Enter Second Name")
print(SecondName , " " ,  FirstName)

#Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
varA=input("Enter ")
varA.split(",")
print(list(varA))
print(tuple(varA))

# Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0] , color_list[-1])

#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
var=input("Enter Number  ")
result=int(var) + int(var+var)+int(var+var+var)
print(result)
#string are added and then converted into integers 

# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
Number = int(input("Enter the number  "))
difference = Number-17
print(difference)
if Number > 17:
    Greater=difference*2
    print(Greater)
elif Number < 17:
    Lesser=abs(difference)
    print(Lesser)

# Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
a=color_list_1.difference(color_list_2)
print(a)

# Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.
# Define a list of numbers.
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
]

# Iterate through the numbers in the list.
for x in numbers:
    if x == 237:
        print(x)  # Print the number if it's 237.
        break  # Exit the loop if 237 is found.
    elif x % 2 == 0:
        print(x)  # Print the number if it's even.


#  Write a Python program that concatenates all elements in a list into a string and returns it.
my_list = ['This', 'is' 'a', 'list', 'of',  'strings']
concatenated_string = ''.join(my_list)
print(concatenated_string)


#. Write a Python program to test whether a passed letter is a vowel or not.
list = ["a","e","i","o","u"]
alphabets=input("Enter Alphabet")
if alphabets in list:
    print("Alphabet is in list")
else:
    print("Not Found")

# Sum of elements, min and max in an array
import array
array=[5,6,7]
print(sum(array))
print(max(array))
print(min(array))

# Length of the list
a = input("Enter: ")
print(list(a))
print(len(list(a)))

#Calculate HCF or GCD
Num_One=int(input("Enter First Number "))
Num_Two=int(input("Enter Second Number "))
if Num_One > Num_Two:
    Minimum=Num_Two
else:
    Minimum=Num_One
for i in range(1 , Minimum+1):
    if Num_One%i == 0 and Num_Two%i ==0:
        HCf=i
print(f"The HCF of {Num_One} , {Num_Two} is {HCf} " )

#agar 8%1 ka remainder 0 hai toh hcf 1 hoga and it goes on 
#HCF=1,2

#Sum of three given integers. However, if two values are equal sum will be zero
def Sum_Three(x,y,z):
    if x==y or y==z or x==z:
        Sum=0
    else:
        Sum=x+y+z
    return Sum
result=Sum_Three(5,6,5)
print(result)

#Sum of two given integers. However, if the sum is between 15 to 20 it will return 20
def special_sum(x, y):
    sum_result = x + y
    if 15 <= sum_result <= 20:
        return 20
    else:
        return sum_result

result = special_sum(10, 6)
print("Result:", result)


# Print an asterisk '*' character on the same line using the 'end' parameter.
# Iterate through a range of numbers from 0 to 9 (inclusive).
for i in range(0, 10):
    print('*', end="")
# Print a newline character to move to the next line.
print()
#by default print doosray line sai start hoga liken hum yahaan per print ko kah rahay hai kai end use karkai aik he line mai print karo


#Add two objects if both objects are an integer type
def Is_Integer(x,y):
    if isinstance(x,int) and isinstance(y,int):
        print("Result" , x+y)
    else:
        print("None")
result=Is_Integer("ali","qasim")


#Add two objects if both objects are an integer type

# Largest Values
a=int(input("Enter"))
b=int(input("Enter"))
c=int(input("Enter"))
print(max(a,b,c))

# Convert into Farenheit
a=int(input("Enter Value "))
farenheit=(a*9/5)+32
print(farenheit)

# Numbers After Swapping 
a=int(input("Enter Number One "))
b=int(input("Enter Number Two "))
print(f"The Numbers before swapping are  {a} , {b}")
temp=a
a=b
b=temp
print(f"The Numbers after swapping are  {a} , {b}")

# Sum of three digits
a=int(input("Enter Number One "))
b=int(input("Enter Number Two "))
c=int(input("Enter Number Three "))
print(a+b+c)
