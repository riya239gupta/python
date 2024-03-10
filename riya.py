#1 illustrate all arithmetic operators
x=int(input("enter x:"))
y=int(input("enter y:"))      
print(x+y)
print(x-y)
print(y**x)
print(x%y)
print(x/y)
print(x//y)
#2 illustrate all logical and relational operators
a=int(input("enter a"))
b=int(input("enter b"))
print((a>b)and (a>=b))
print(a<b)
print((a==b)or(a>b))
print(a!=b)
print(a>=b)
print(a<=b)
#3 table of 5 upto user's choice
n=int(input("enter the number for table"))
for i in range(1,n+1):
    print('5','x', i, '=', (5*i))
#4 given number is even or odd
def even(r):
    if r%2==0:
        print("even number")
    else:
        print("odd number")
r=int(input("enter a number"))
print(even(r))
#5 leap year or not
q=int(input("enter the year"))
if q%400==0:
    print("leap year")
elif q%4==0 and q%100!=0 :
    print("leap year")
else:
    print("not a leap year")
#6 prime or composite
num=int(input("enter a number:"))
if num>1:
    for i in range (2, num):
        if(num%i)==0:
            print(num, "composite number")
            break
        else:
            print(num,"prime number")
else:
     print(num,"not prime")
#7 sum of first n natural terms
num=int(input("enter the number:"))
s=0
for i in range(1,num+1):
    s=s+i
print(s)
#8 factorial of a given number
def fact(num):
    product=1
    for i in range(1,num+1):
        product = product*i
    print(product)
num=int(input("enter the number:"))
fact(num)
#9 sum of digits of a given number
def getsum(n):
    sum=0
    while(n!=0):
        sum=sum+(n%10)
        n=n//10
    return sum
n=int(input("enter a number"))
print(getsum(n))
#10 to find reverse of a given number
n=1234
print(str(n)[::-1])
num=int(input("enter a number"))
rnum=0
while num!=0:
    d=num%10
    rnum=rnum*10+d
    num//=10
print("reverse:",str(rnum)) 
#11 pallindrome or not
n=int(input("enter a number:"))
temp=n
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
if(temp==rev):
    print("pallindrome")
else:
    print("not pallindrome")
#12 print fibonacci series upto n terms
n= int(input("enter the number:"))
n=10
a=0
b=1
next_num=b
count=1
while count<= n:
    print(next_num,end=" ")
    count+=1
    a,b=b,next_num
    next_num=a+b
print()
#13 first 100 even numbers
for i in range(0,101):
    if(i%2==0):
        print(i)
#14 armstrong number
num=int(input("enter a number"))
sum=0
temp=num
while temp>0:
    d=temp%10
    sum+=d**3
    temp//=10
if num == sum:
    print("armstrong")
else:
    print("not armstrong")
#15 all pallindrome from 500 to 1000
for n in range(500,1000):
    temp=n
    rev=0
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
    if(temp==rev):
        print(temp)
#16 patterns
#a
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r") 
#b
def pattern(n):
    for i in range(n,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print("\r") 
print(pattern(5))
#c
height = 5
for row in range(1, height+1):
    if(row%2!=0):
        print(" " * (height-row)+" *"*row)  
#d 
num=1
n=5
for i in range (0,n):
    for j in range (0,i+1):
        no=int(num)
        print(no,end=" ")
    num=num+1
    print("\r")
#pascal's triangle
from math import factorial
n=5
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//factorial(j)*factorial(i-j),end=" ")
    print()
# floyd's triangle
def ft(n):
    val=1
    for i in range(1,n+1):
        for j in range (1,i+1):
            print(val,end=" ")
            val+=1
        print(" ")
ft(7)
#17 scripts using functions
#a pallindrome
def pallindrome(n):
    
    temp=n
    rev=0
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
    if(temp==rev):
        print("pallindrome")
    else:
        print("not pallindrome")
n=int(input("enter a number:"))
print(pallindrome(n))
#b sum of n natural numbers
def sum(num):
    s=0
    for i in range(1,num+1):
        s=s+i
    print(s)
#18 python codes for
#a decimal to binary
def func(num):
    if num >1:
        func(num//2)
    print(num%2,end=' ')  
a=int(input("enter a decimal number:"))
print(func(a))
#b decimal to octal
def func(num):
    if num<=0:
        return ''
    else:
        func(num//8)
        print(num%8, end=' ')
a=int(input("enter a decimal number:"))
print(func(a))
#c factorial using recursion
def fact(num):
    product=1
    for i in range(1,num+1):
        product = product*i
    print(product)
num=int(input("enter the number:"))
fact(num)
#d fibonacci recursion
def fib(n):
    if n<= 1:
        return n
    else:
        return(fib(n-1)+fib(n-2))
n=10
for i in range(n):
    print(fib(i))
#e GP
def gp(a, r, n):
    sum=0
    for i in range(0,n):
        term=a*pow(r,i)
        print(term,end=" ")
        sum=sum+term
    print("\n""the sum is ",sum)
        
a=int(input("enter the first term ")) 
r=int(input("enter the common ratio"))
n=int(input("enter the nth term"))
gp(a,r,n)
#19 sum of terms of a numeric list
l=[2,4,5,8,3]
print(sum(l))
#20 finding smallest and larest from a list
l=[]
while(True):
    a=int(input("enter number the loop will break on entering a negative number"))
    if a<0:
        break
    else:
        l.append(a);
print(l);
large=small=l[0]
for i in l:
    if i>large:
        large=i
    if i<small:
        small=i
print("largest number:",large)
print("smallest number:",small)
# 21 removing duplicates
l=[1,2,3,4,1,6,7,6,8]
print("original list"+str(l))
res=[]
[res.append(x) for x in l if x not in res]
print("after removing duplicates:"+str(res))
#22 list concatination
def li(lst,n):
    l1=[item+str(i) for i in range(1,n+1) for item in lst]
    return l1
l=['p','q']
n=5
res=li(l,n)
print(res)
#23 matrix transpose
x=[[1,2,4],[4,5,6],[7,0,9]]
y=[[6,3,7],[8,3,9],[3,2,9]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for row in range(len(x)):
    for column in range(len(x[0])):
        result[row][column]=x[column][row]
for r in result:
    print(r)
#24 matrix addition
x=[[1,2,4],[4,5,6],[7,0,9]]
y=[[6,3,7],[8,3,9],[3,2,9]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for row in range(len(x)):
    for column in range(len(x[0])):
        result[row][column]=x[row][column]+y[row][column]
for r in result:
    print(r)
#25 matrix multiplication
x=[[1,2,3],[4,5,6], [7,8,9]]
y=[[1,2,3],[4,5,6], [7,8,9]]
result=[[0,0,0],[0,0,0], [0,0,0]]
for i in range(len(x)):
    for j in range(len((x)[0])):
        for k in range (len(y)): 
            result[i][j] += x[i][k]*y[k][j]
for r in result:
    print(r)
#26 lambda function (power of 2)
l1=[2,3,8,4,1]
result=map(lambda x:x*x,l1)
print(list(result))
#27 numbers in a list that are divisible by a particular number
l=[24,56,31,90,13,67,33]
result=[x for x in l if x%2==0]
print(result)
#28 even number from 1 to 20 by list comprehension
l=[x for x in range(0,21) if x%2==0]
print(l)
#29 table of 10 until user want by list comprehension
n=int(input("enter the number for table"))
res=[10*i for i in range(1,n+1)]
print(res)
# with lambda function
li=[]
n=int(input("enter the number"))
for i in range (0,n+1):
    li.append(i)
print(li)
table=map(lambda x:x*10,li)
for j in table:
    print(j,end=" ")
#30 check weather a list is sorted or not
l1=[4,5,8,1,9,2]
l2=l1.sort
if l1==l2:
    print("list sorted")
else:
    print("list unsorted")
