Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
b=92.25
int(b)
92
complex(b)
(92.25+0j)
str(b)
'92.25'
list(b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
c=3+4j
int(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(3+4j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
s='codegnan'
int(s)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
float(s)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'codegnan'
complex(s)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
list(S)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    list(S)
NameError: name 'S' is not defined. Did you mean: 's'?
tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
set(s)
{'e', 'o', 'n', 'g', 'c', 'a', 'd'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
l=[1,2,3,4,5,"abcd"]
int(l)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
str(l)
"[1, 2, 3, 4, 5, 'abcd']"
tuple(l)
(1, 2, 3, 4, 5, 'abcd')
set(l)
{1, 2, 3, 4, 5, 'abcd'}
dict(l)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
t=(1,2,3,4,5,6,"acdf")
int(t)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
str(t)
"(1, 2, 3, 4, 5, 6, 'acdf')"
list(t)
[1, 2, 3, 4, 5, 6, 'acdf']
set(t)
{1, 2, 3, 4, 5, 6, 'acdf'}
dict(t)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True
d={1,2,3,4,("abcd")}
int(d)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(d)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'set'
complex(d)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'set'
str(d)
"{1, 2, 3, 4, 'abcd'}"
list(d)
[1, 2, 3, 4, 'abcd']
tuple(d)
(1, 2, 3, 4, 'abcd')
dict(d)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    dict(d)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(d)
True
r={'Name':'john','Batch':63,'Course':'PFS'}
int(r)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    int(r)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(r)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    float(r)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(r)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    complex(r)
TypeError: complex() first argument must be a string or a number, not 'dict'
str(r)
"{'Name': 'john', 'Batch': 63, 'Course': 'PFS'}"
>>> list(r)
['Name', 'Batch', 'Course']
>>> tuple(r)
('Name', 'Batch', 'Course')
>>> set(r)
{'Name', 'Course', 'Batch'}
>>> bool(r)
True
>>> q=True
>>> int(q)
1
>>> float(q)
1.0
>>> complex(q)
(1+0j)
>>> str(q)
'True'
>>> list(q)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    list(q)
TypeError: 'bool' object is not iterable
>>> tuple(q)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    tuple(q)
TypeError: 'bool' object is not iterable
>>> set(q)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    set(q)
TypeError: 'bool' object is not iterable
>>> dict(q)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    dict(q)
TypeError: 'bool' object is not iterable
