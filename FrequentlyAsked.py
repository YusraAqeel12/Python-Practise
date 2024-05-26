# How To Swap 2 Numbers
Num_One=5
Num_Two=6
print(Num_One , "Is Number One before Swapping")
print(Num_Two , "Is Number Two before Swapping")
Temp=Num_One # 5 in Temp
Num_One=Num_Two  #6 in Num_One
Num_Two=Temp
print(Num_One , "Is Number One after Swapping")
print(Num_Two , "Is Number Two after Swapping")

# How To Find Factorial of A Number
#1*2*3*4*5
factorial=1
Number=5
if Number<0:
    print("Factorial Cant be negetive")
elif Number == 0:
    print("Factorial of 0 is One")
else:
    for i in range(1,Number+1): #Range 6 tak chalay gee q kai for loop mai 2 parameter mai us ka pehla waala consider hota hai 
        factorial=factorial*i
    print("The Factorial of number is" , factorial)

#agar range 11 tak likhtay toh 10 tak print hota 


# Program to Print Fibonacci Series - 
number=int(input("Enter Number: "))
x=0 
y=1
z=0 
#agar z chota haui number sai toh z print karo x hogaya 1 and y hogaya 0 and then z mai add hoga toh it becomes one
#loop us waqt taq chalay gaa ga jab tak z becomes greater than number
while z<number:
    print(z)
    x=y
    y=z
    z=x+y

# Swap first and lst in list
myList=list(input("Enter "))
First=myList[0]
Last=myList[-1]
print("before swapping" , First , Last)
temp=First
First=Last
Last=temp
print(myList)
print("after swapping", First,Last)

# How To Search an Element in a List
my_list=list(input("Enter The List : "))
element_to_find=input("Enter Element ")
if element_to_find in my_list:
    print("Found")
else :
    print("Not Found")

# How To Clone or Copy a List
a=list(input("Enter: "))
a_copy = a[:]
print(a_copy)

#Find number of occurence of a number in a list
# Count returns number of times object appears in a list
a = ['5', '6', '7', '8', '9', '9', '9']   
b = '9'  # Convert to string
print(a.count(b))


#Multiply All Numbers in the List
my_list=[7,8,]
result=1
for i in my_list:
    result=result*i
print(result)

#Check if palindrome 
a=input("Enter String ")
reverse=a[::-1]  #a ko reverse karo and then store
if reverse == a:
    print("palindrome")
else :
    print("Not palindrome")
# hello world
# when using split 
#input liya aur split kiya toh it become ['hello' , 'world']
# jab reverse karogay toh it becomes ['world']
# so now you are comparing it with palindrome which is wrong


#Reverse of a string
#Splitt method split string into list
#Join method takes all items and joins them into a string
Your_input=input("Enter ")
splitting=Your_input.split()
print(splitting)
reverse=splitting[::-1]
print(reverse)
joinning="".join(reverse)

#Find Sub string Presence in a String
#The find() method finds the first occurrence of the specified value.
#The find() method returns -1 if the value is not found.
string=input("Enter ")
substring=input("Enter Substring ")
FindSubstring=string.find(substring)
print(FindSubstring)
if FindSubstring == -1:
    print("Substring Not Found")
else :
    print("Substring Found")

#Find length of the string 
string=input("Enter ")
counter=0
for i in string:
    counter=counter+1
print(counter)


#Check of the inputs are anagram
#Anagram have length equal and have same number of characters 
#abc acb are anagram

string_one=input("Enter String One ")
string_two=input("Enter String Two ")

if len(string_one) != len(string_two):
    print("Not An Anagram")
else :
     sorted(string_two) == sorted(string_one)
     print("Is Anagram")

# Code to find if a string is symmetrical and palindrome
# Symmetrical tells us about kai dono halves of input same hain ya nahi
# len(a) gives us only the total number of character in string
a = input("Enter ")
# b doesnot convert a string into list
# string mai bhee slicing hoti hai 
b = a[::-1]
print(len(a))
if a == b and len(a) % 2 == 0:
    print("Palindrome and Symmetrical")
elif a == b and len(a) % 2 != 0:
    print("Palindrome but not symmetrical")
elif len(a) % 2 == 0 and a != b:
    print("Symmetrical but not palindrome")
else:
    print("Not Symmetrical and not palindrome")

def sym_pal(string):
    if string == string[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")
    a=len(string)
    if a % 2 == 0:
        print("Symmetrical")
    else:
        print("Not a symmetrical")
sym_pal('amaama')

# Method to remove a character from the string
# Replace method replaces string or a character with anything
def removal(strOne, strTwo):
        print (strOne.replace(strTwo , " "))
strOne=input("Enter the string")
strTwo=input("enter character ")
removal(strOne,strTwo)

# Method to print even characters of a string
# You cant use list q kai her element list mai convert hogai gaa jiska length one hoga
# split method splits string into list
# list splits all elements into list
a=input("enter ")
c=list(a)
print(c)
b=a.split()
for i in b:
    if len(b) % 2 == 0:
        print(i)

# Given a String, perform uppercase of the later part of the string.
a=input("Enter ")
b=a.split()   #['yusra' , 'aqeel']
c=b[-1]       # aqeel which is tupple here agar list mai chahiyae toh use [-1:]==>['aqeel']
# join elements into a single string
print(c.upper())

# Python program to capitalize the first and last character of each word in a string
a=input("Enter ")
b=a.split()
c=b[0] , b[-1] 
d=" ".join(c) # join elements into a single string
print(d.title())

# Python Program to Accept the Strings Which Contains all Vowels
def check_string(string):
    string=string.lower()   #convert input into lower case
    vowels=set("aeiou")     #vowels ka var liya aur usmai set banaliyae
    s=set()               #empty set liya 
    for i in string:        #iterate over each character of string 
        if i in vowels:     #agar hamara character vowels mai hai
            s.add(i)        #empty set mai add kardo us character ko
        else:
            break
    if len(s) == len(vowels):
        print("accepted")
    else:
        print("rejected")
           
string="aeioubjncdbc"
check_string(string)

# Python program to check if a string has at least one letter and one number
def check_string(string):
    flagOne=False
    flagTwo=False
    for i in string:
        if i in "abcdefghijklmnopqrstuvwxyz":
            flagOne=True
        
        if i in "9876543210":
            flagTwo=True
    return(flagTwo,flagOne)
string="yusraaqeel089"
print(check_string(string))

def function(string):
    flagOne=False
    flagTwo=False
    string=string.lower()
    for i in string:

        if i.isalpha():
            flagOne=True
        
        if i.isdigit():
            flagTwo=True

    return(flagOne , flagTwo)
string='YusraAqeel090'
print(function(string))
# There is a difference in IN and == 
# In is used to test is the value exist in a sequence
# == Checks if the values are equal

# Python | Count the Number of matching characters in a pair of string
def common_func(stringOne , stringTwo):
    stringOne=stringOne.lower()
    stringTwo=stringTwo.lower()
    a=set(stringOne).intersection(set(stringTwo))
    return len(a)

common_Character=common_func('abc' , 'abc')
print(common_Character)
# Common caharcters kai liyae split nahi karna 
# coomon strings kai liyae split string into list of words

# Find minimun frequency of characters in astring
def count_fre(str):
    str=str.lower()
    a={}
    for i in str:
        if i == a:
            a[i]=i+1
        else:
            a[i]=1
    return  min(a , key=a.get)  #agar a ko print karain toh output will be {'a': 1, 'b': 1, 'j': 1, 'd': 1, 'h': 1, 'c': 1}
# yahaan min ka matlab min alphabet hai
str=count_fre("abjdhabchjd")
print(str)


# Count total  number of String
res=0
digits="0123456789"
for i in test_str:
	if(i in digits):
		res+=1
# printing result
print("Count of numerics in string : " + str(res))

# Find words which are greater than given length k
def func(str, number):
    str = str.split(' ')
    a = []
    for i in str:
        if len(i) > number:
            a.append(i)
    return a

a = func("hello geeks for geeks", 3)
print(a)

# Code to find url of an input string 
# Python code to find the URL from an input string

def Find(string):
	x=string.split()
	res=[]
	for i in x:
		if i.startswith("https:") or i.startswith("http:"):
			res.append(i)
	return res
			
# Driver Code
string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
print("Urls: ", Find(string))

# uncommon word in string
# Python3 program to find a list of uncommon words

# Function to return all uncommon words
def UncommonWords(A, B):	
	# split the strings A and B into words and create sets
	setA = set(A.split())
	setB = set(B.split())
	# find the uncommon words in setA and setB and combine them
	uncommonWords = setA.difference(setB).union(setB.difference(setA))
	# convert the set to a list and return
	return list(uncommonWords)
# Driver Code
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
# Difference mai A-B matlab common words hat jaingay and sirf A set kai
# words jo uncoomon hai wo print hongay
# Print required answer
# We first split string A into list of words and the convert into set
print(UncommonWords(A, B))
