#Given an integer perform the following conditional actions:
#If  is odd, print Weird
#If  is even and in the inclusive range of 2 to 5, print Not Weird
#If  is even and in the inclusive range of 6 to 20, print Weird
#If  is even and greater than 20 , print Not Weird

#// performs floor division 7//2 is 3 ,% gives remainder 7%2=1

n=int(input("Enter Number : "))
if n % 2 != 0 :
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

# The list of non-negative integers that are less than  3 is 0,1,2. Print the square of each number on a separate line.
n=int(input("Enter: "))
for i in range(0,n):
    print( i * i)

def is_leap(year):
    if year%4==0:
        if year%100==0 and year%400==0:
            leap = True
        else:
            leap = False
    else:
        leap = False
    return leap

#Print input number in one line
def print_sequence_without_spaces(n):
    for i in range(n + 1):
        print(i, end="")
n = int(input("Enter: "))
print_sequence_without_spaces(n)

