Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
c='strings.py'
c.startswith('str')
True
c.startswith('python')
False
c.endswith('py')
True
c.endswith('python')
False
c.islower()
True
c.isupper()
False
'PYTHONV13'.isupper()
True
c.isalpha()
False
's123'.isalnum()
True
's.123'.isalnum()
False
'        '.isspace()
True
'h       '.isspace()
False
'this is title'.istitle()
False
'This Is Title'.istitle()
True
'my@var'.isidentifier()
False
'my_var'.isidentifier()
True
>>> l=[]
>>> l=list()
>>> l=[1,12.3,2+3j,'str',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,2:3},None,True]
>>> l
[1, 12.3, (2+3j), 'str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 3}, None, True]
>>> l=[1,1,1,1,1]
>>> l
[1, 1, 1, 1, 1]
>>> type(l)
<class 'list'>
>>> l=[1,2,3,4]
>>> m=[5,6,7]
>>> l+m
[1, 2, 3, 4, 5, 6, 7]
>>> m*3
[5, 6, 7, 5, 6, 7, 5, 6, 7]
>>> l
[1, 2, 3, 4]
>>> l[3]
4
>>> l[-1]
4
>>> l[-1]
4
>>> l[1:]
[2, 3, 4]
>>> l[:2]
[1, 2]
>>> l[::-1]
[4, 3, 2, 1]
>>> '6' not in l
True
>>> '4' in l
False
