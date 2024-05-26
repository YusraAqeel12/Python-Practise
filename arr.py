# Max and Min elements in an array
# array liya jiska len nikaala by default max is array ka first index
# max here is number which is in 0 index 
# agar hamara max bara hai hamari iteration sai toh max wo iteration hogai gee 
# and same goes on and one

arr=[8,6,9,7,0]
n=len(arr)
print(arr[0])
max=arr[0] #arr with 0 index is 8
for i in range(1 , n):
    if max < arr[i]:
        max = arr[i]
print(max)
# starts with arr one iteration which is 6

# Min Array
arr=[8,6,9,7,0]
n=len(arr)
min=arr[0]
for i in range(1 , n):
    if min > arr[i]:
        min = arr[i]
print(min)

# First three highest values 
def func(arr):
    n=len(arr)
    if n < 3:
        print("Not Possible")
        return
    first = second =third= float('-inf')
    for i in range(n):
        if arr[i] > first:
            third=second
            second=first
            first=arr[i]
        
        elif arr[i] > second and arr[i] != first:
            third = second
            second = arr[i]
        
        elif arr[i] > third and arr[i] != second and arr[i] != first:
            third = arr[i]
    
    print("First , Sec , Third Values are" , first ,second , third)
arr=[0,8,5,9]
func(arr)

# kiya twelve first sai bara hai yes it is toh sec -ve is third first
# -ve is second and first is our iteration  
# first = 0   8   9
# second =-ve 0  8
# third =-ve -ve  0

# == is for comparision = is used for assignment\

# Find second largest in an array 
def func(arr):
    n=len(arr)
    if n < 3:
        print("Not Possible")
        return
    arr.sort(reverse=True) 
    for i in range(n):
        if arr[i] != arr[0]:
            print("The largest element in the array is" , arr[i])
            return

arr=[0,8,7,9]
func(arr)

# sorted array = [0, 7, 8, 9]
# sorted reverse = [9, 8, 7, 0]
# here arr[i] is sorted reverse array q lkai wo array main initialize howa hai 
# When i = 0, arr[i] is 9 and arr[0] is also 9.
# When i = 1, arr[i] is 8 and arr[0] is 9.
# When i = 2, arr[i] is 7 and arr[0] is 9.
# When i = 3, arr[i] is 6 and arr[0] is 9.
# When i = 4, arr[i] is 0 and arr[0] is 9.

# Program to find common in both arrays

# agar mairy itearions array two mai hai liken common mai nahi hai
def function(arrone , arrtwo):
    common=[]
    for i in arrone:
        if i in arrtwo and i not in common:
            common.append(i)
    print (common)
    return
arrone=[9,8,7]
arrtwo=[9,6,8]
function(arrone,arrtwo)
# functions kai saath parameters hona zaroori hai
# agar mairy itearions array two mai hai liken common mai nahi hai
# print will come outside for loop , inside sirf aik iteration pass hogi
# toh add kardo and print karwaao

# remove duplicates from array
def remove(arr):
    seen=set()
    result=[]
    for i in arr:
        if i not in seen:
            seen.add(i)
            result.append(i)
    print(result)
    return
    
arr=[9,7,8,0,6,0,9]
remove(arr)
# empty set banaigay and result ka aaray banai gay
# itearate over string agar hamara i nahi hai seen mai toh add kardo and 
# result array main add kardo agar i hai seen ya result array mai toh 
# doosri iteration per jaaon is tarah sai unique elemets millingay
# you can still remove seen set but using only array is less efficient

# FInd Duplicates
def find_duplicates(arr):
    seen = set() 
    duplicates = []
    for i in arr:
        if i in seen and i not in duplicates:
            duplicates.append(i)
        else:
            seen.add(i)
    return duplicates
# Example usage
arr = [1, 3, 2, 1, 5, 2, 7, 3]
duplicates = find_duplicates(arr)
print("Duplicates:", duplicates)
# 1 3 2

# When i is 1, it's not in seen yet, so it's added to seen.
# When i is 3, it's not in seen yet, so it's added to seen.
# When i is 2, it's not in seen yet, so it's added to seen.
# When i is 1 again, it's already in seen, so it's a duplicate. But since it's not in duplicates yet, it's added to duplicates.
# Similarly, 2 and 3 are also added to duplicates because they are already in seen but not yet in duplicates.
# Therefore, duplicates will contain [1, 2, 3], which are the duplicate elements in the array.

# Find Number of even / odd in an array
def function(arr):
    n=len(arr)
    counteven=0
    countodd=0
    for i in range(n):
        if arr[i]&1 == 1:
            countodd=countodd+1
        else:
            counteven=counteven+1
    print(f"The Number of even are {counteven} The Number of odd are {countodd}" )
    return
arr=[9,8,7,6,5,0]
function(arr)

# Find reverse of an array
def function(arr, s ,e):
    while e > s:
        arr[s] , arr[e] = arr[e] , arr[s]
        s=s+1
        e=e-1
    print(arr)
    return
arr=[9,8,7,6,5]
s=0
e=len(arr)-1
function(arr,s,e)
# list index ka error aayi gaa q kai e should be len(arr) -1
# arr[s] here is 9 and arr[e] here is 5
# Original list: [9, 8, 7, 6, 5]
# After the first swap (start = 0, end = 4):
# arr[start] (9) and arr[end] (5) are swapped: [9, 8, 7, 6, 5] -> [5, 8, 7, 6, 9]
# After the second swap (start = 1, end = 3):
# arr[start] (8) and arr[end] (6) are swapped: [5, 8, 7, 6, 9] -> [5, 6, 7, 8, 9]
# Reversed list: [5, 6, 7, 8, 9]

# Find Missing Array
def find_missing_number(arr):
    n = len(arr) + 1  # The length of the array is n - 1, so the expected length is n
    expected_sum = n * (n + 1) // 2  # Sum of numbers from 1 to n
    
    actual_sum = sum(arr)  # Sum of numbers in the array
    missing_number = expected_sum - actual_sum  # Find the missing number
    
    return missing_number

# Example usage
arr = [1, 2, 4, 5, 6]
missing = find_missing_number(arr)
print("The missing number is:", missing)

# merge two sorted array
# sum twos
# find os and is and two

# Sum of element of an array
def array_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Example usage:
array = [1, 2, 3, 10]
print(array_sum(array))  # Output: 16

# take two inputs of an array such that remove element from the second array because of first array
def remove_common_elements(arr1, arr2):
    # Convert the first array to a set for faster lookup
    arr1_set = set(arr1)
    # Iterate over a  copy of the second array to safely remove elements
    for num in arr2[:]:  # Iterating over a copy to safely remove elements
        if num in arr1_set:
            arr2.remove(num)
# Example usage:
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
remove_common_elements(arr1, arr2)
print("Array 1:", arr1)
print("Array 2:", arr2)

