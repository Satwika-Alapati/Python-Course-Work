Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#int float str list tuple set dict
x=input()
asdf
x
'asdf'
name=input()
satwika
name
'satwika'
name=input("Enter your name: ")
Enter your name: satwika
name
'satwika'
age=input("Enter the age: ")
Enter the age: 21
age
'21'
age=int(input("Enter the age: "))
Enter the age: 21
age
21
type(age)
<class 'int'>
price=input("Enter the price: ")
Enter the price: 99.99
price
'99.99'
price=float(input("Enter the price: "))
Enter the price: 99.99
price
99.99
names=input("Enter the names: ")
Enter the names: satwika codegnan pfs
names
'satwika codegnan pfs'
names.split()
['satwika', 'codegnan', 'pfs']
names=input("Enter the names: ").split()
Enter the names: satwika codegnan pfs
names
['satwika', 'codegnan', 'pfs']
names=input("Enter the names: ").split()
Enter the names: 1 2 3 4 54 5
names
['1', '2', '3', '4', '54', '5']
map(int,names)
<map object at 0x0000029E73151A80>
list(map(int,names))
[1, 2, 3, 4, 54, 5]
values=list(map(int,input().split()))
1 2 34 5 5 6556754
values
[1, 2, 34, 5, 5, 6556754]
values=list(map(float,input().split()))
1 2 3454 5463.23
values
[1.0, 2.0, 3454.0, 5463.23]
names=tuple(input("Enter the names: ").split())
Enter the names: fghj fdghj fgh
names
('fghj', 'fdghj', 'fgh')
values=tuple(map(int,input().split()))
1 2 3 4
values
(1, 2, 3, 4)
values=tuple(map(float,input().split()))
567 5678 567
values
(567.0, 5678.0, 567.0)
names=set(input().split())
ytuio true tyu
names
{'true', 'tyu', 'ytuio'}
values=set(map(int,input().split()))
1 2 3 4
values
{1, 2, 3, 4}
values=set(map(float,input().split()))
1 2 4 4
values
{1.0, 2.0, 4.0}
a,b=[1,2]
a
1
b
2
a,b=(1,2)
a
1
b
2
email,password=input("Enter the email and password: ").split()
Enter the email and password: satwika@gmail.com 12345
email
'satwika@gmail.com'
password
'12345'
a,b,c=list(map(int,input().split()))
1 2 3
a
1
b
2
c
3
name,marks=input().split()
satwika 89
name
'satwika'
marks
'89'
int(marks)
89
e=eval(input())
1
e
1
e=eval(input())
1234.13
e
1234.13
>>> e=eval(input())
"satwika"
>>> e
'satwika'
>>> e=eval(input())
[1,2,3,4,4,5]
>>> e
[1, 2, 3, 4, 4, 5]
>>> e=eval(input())
[1,12.4,"str",[1,2,3]]
>>> e
[1, 12.4, 'str', [1, 2, 3]]
>>> e=eval(input())
(1,2,4,3)
>>> e
(1, 2, 4, 3)
>>> e=eval(input())
[1,2,3,4,5]
>>> e
[1, 2, 3, 4, 5]
>>> e=eval(input())
{1,2,3,4,5}
>>> e
{1, 2, 3, 4, 5}
>>> e=eval(input())
{1:1,2:2,3:3}
>>> e
{1: 1, 2: 2, 3: 3}
>>> e=eval(input())
True
>>> e
True
>>> e=eval(input())
2+3*4+5*8
>>> e
54
