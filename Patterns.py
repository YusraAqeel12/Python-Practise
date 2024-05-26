
#Print Stars while incrementing
a=1
i=1
while i <=5:
    print(str(a)  * i)
    i=i+1

a=1
i=1
while i <=5:
    print(str(a)  * i)
    i=i+1
    a=a+1

for a in range(5):
    for b in range(a+1):
        print (b , end="")
    print()

#Question One
a=0
for i in range(5):
    print(str(a)*i)
    a=a+1

#Question Three
a=1
for i in range(5,0,-1):
    print(str(a)*i)
    a=a+1


#Print a star
print("*")

#Print a star 5 times:
n=5
print((n) * "*")

#Print a star 5 times vertically using for loop:
for i in range(6):
    print("*")

#Print 5 stars horizontally using for loop:
for i in range(6):
    print("*" , end="")

#Print a Square
for i in range(5):
    for b in range(5):
        print("*" , end="")
    print()

#Increasing Triangles
n=5
for i in range(n):
    for j in range(i+1):
        print("*" , end="")
    print()

#Decreasing Triangles
n=5
for i in range(n):
    for j in range(i ,n):
        print("*" , end="")
    print()
# Half Pyramid Left Patterns Increasing
n=6
for i in range(1,n):
    for j in range(1,i+1):
        print("*" , end="")
    print('\n')
#assume outer loop is i loop it print lines kai hamara program 5
# lines tak chalay gaa 
# assume j kai wo * print karay gaa jo chalay ka one sai 5 tak
# iteration is one toh will print first star and 
# To change line print n jo j loop kai baahir hai Star print karo and then line changes

# Half Pyramid Patterns Left Decreasing 
n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*" , end="")
    print('\n')
# ith loop will go from 5 to 1 but backwards
# First iteartion is the jth loop will print stars from 1 till 5

#Left Pyramids And Middle Pyramids and Right Pyramids
#Increase the space in i ka star 
n=5
m=n
for i in range(0,n):
    print(""*m , "*" *i)
    m=m-1


# Half Pyramid Right Increasing Order
n=6
for i in range(1,6):
    for k in range(1,n-i):
        print(" " ,end="")
    for j in range(1,i+1):
        print('*' , end="")
    print('\n')
# K loop will print space jo chalay one sai 6-i tak 
# first iteration mai 5 space print hongay and one star print hoga

# Full Pyramids
n=6
for i in range(1,6):
    for k in range(1,n-i):
        print(" " ,end="")
    for j in range(1,(2*i-1)+1):
        print('*' , end="")
    print('\n')
# Range will go from When i = 1, (2*i - 1) + 1 equals 1 + 1 = 2.
# This means the range will go from 1 to 2, including 1 and 2.
# It prints one asterisk (*) as expected.

# Half Pyramid Right Numbers
def left_aligned_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Example usage
left_aligned_pyramid(5)

# Half Pyramid Right Numbers number adding
def number_pyramid(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

# Example usage
number_pyramid(5)

