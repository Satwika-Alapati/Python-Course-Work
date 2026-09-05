Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
count=10
count=7
count
7
type(count)
<class 'int'>
price=99.99
price
99.99
type(price)
<class 'float'>
c=3+8j
c
(3+8j)
c=4+9J
c
(4+9j)
type(c)
<class 'complex'>
s='codegnan'
s
'codegnan'
type(s)
<class 'str'>
l=[]
l=list()
type(l)
<class 'list'>
l=[1,2,3,4,5,6,"asdfg",7555.555,[1,2,3,4],(1,2)]
l
[1, 2, 3, 4, 5, 6, 'asdfg', 7555.555, [1, 2, 3, 4], (1, 2)]
type(l)
<class 'list'>
t=()
t=tuple()
type(t)
<class 'tuple'>
t=(1,2,3,4,5,6,"qwert",77.20,(1,2))
t
(1, 2, 3, 4, 5, 6, 'qwert', 77.2, (1, 2))
type(t)
<class 'tuple'>
s={}
s=set{}
SyntaxError: invalid syntax
>>> s=set()
>>> type(s)
<class 'set'>
>>> s={1,1,1,1}
>>> s
{1}
>>> s={"Name":"satwika","Course":"PFS","Batch":63}
>>> s
{'Name': 'satwika', 'Course': 'PFS', 'Batch': 63}
>>> type(s)
<class 'dict'>
>>> KeyboardInterrupt
>>> s={"swerfgtyh",456.12,("asdf")}
>>> s
{456.12, 'asdf', 'swerfgtyh'}
>>> type(s)
<class 'set'>
>>> status=True
>>> type(status)
<class 'bool'>
>>> status=None
>>> type(status)
<class 'NoneType'>
>>> s=[1,2,3,4,5]
>>> s
[1, 2, 3, 4, 5]
>>> s.add(6)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s.add(6)
AttributeError: 'list' object has no attribute 'add'
>>> s.remove(2)
>>> s
[1, 3, 4, 5]
>>> s=frozenset({1,2,3,4})
>>> s
frozenset({1, 2, 3, 4})
