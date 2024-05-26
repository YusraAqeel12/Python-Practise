def cal_sum(a,b):
    Sum = a+b
    print(Sum)
cal_sum(7,0)
cal_sum(8,7)
cal_sum(7,6)

#Return karnay kai baad you need to put function name in a variable and then print it
def Cal_Sum(c,d):
    return c+d
Sum=Cal_Sum(9,0)
print(Sum)

def printing():
    print("Hello")
printing()

def avg(e,f,g):
    return e+f+g/3
average=avg(1,1,1)
print(average)

# Recursive Function 
def show(n):
    if n == 0:
        return n
    print(n)
    show(n-1)
show(5)