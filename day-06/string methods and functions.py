Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
c='python programming'
len(c)
18
ord('p')
112
ord('a')
97
ord('0')
48
ord('A')
65
chr(65)
'A'
chr(66)
'B'
chr(50)
'2'
min(c)
' '
max(c)
'y'
sorted(c)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
c='String is immutable'
c
'String is immutable'
c.upper()
'STRING IS IMMUTABLE'
c.lower()
'string is immutable'
c.capitalize()
'String is immutable'
c.title()
'String Is Immutable'
c.swapcase()
'sTRING IS IMMUTABLE'
'STRAẞEMÁLAGAÅngströmCafe'.casefold()
'strassemálagaångströmcafe'
c
'String is immutable'
c.centre(60,'-')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    c.centre(60,'-')
AttributeError: 'str' object has no attribute 'centre'. Did you mean: 'center'?
c.center(60,'-')
'--------------------String is immutable---------------------'
c.center(60,'*')
'********************String is immutable*********************'
c.center(60,'0')
'00000000000000000000String is immutable000000000000000000000'
d.ljust(60,'-')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d.ljust(60,'-')
NameError: name 'd' is not defined. Did you mean: 'id'?
c.ljust(60,'-')
'String is immutable-----------------------------------------'
c.rjust(60,'-')
'-----------------------------------------String is immutable'
'12'.zfill(4)
'0012'
'12'.zfill(10)
'0000000012'
'123456'.zfill(5)
'123456'
'456'.zfill(5)
'00456'
c
'String is immutable'
c.find()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    c.find()
TypeError: find() takes at least 1 argument (0 given)
c.find
<built-in method find of str object at 0x000001B861954770>
c.find('S')
0
c.find('i')
3
c.find('z')
-1
c.rfind('i')
10
c.index('z')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    c.index('z')
ValueError: substring not found
c
'String is immutable'
c.count('i')
3
c
'String is immutable'
c.count('g')
1
c.count('m')
2
c
'String is immutable'
c.replace('i','0')
'Str0ng 0s 0mmutable'
c.replace('String','Float')
'Float is immutable'
c.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.translate(c.maketrans('aeiou','12345'))
'Str3ng 3s 3mm5t1bl2'
c.translate(c.maketrans('aeiou','*****'))
'Str*ng *s *mm*t*bl*'
c
'String is immutable'
c.split()
['String', 'is', 'immutable']
'String is immutable'
'String is immutable'
'String,is,immutable'.split()
['String,is,immutable']
'String,is,immutable'.split(',')
['String', 'is', 'immutable']
'String-is-immutable'.split('-')
['String', 'is', 'immutable']
'String is immutable'.split()
['String', 'is', 'immutable']
'String is immutable'.rsplit()
['String', 'is', 'immutable']
'String is immutable'.rsplit('",1)
                             
SyntaxError: unterminated string literal (detected at line 1)
'String is immutable'.rsplit('',1)
                             
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    'String is immutable'.rsplit('',1)
ValueError: empty separator
'String is immutable'.rsplit(' ',1)
                             
['String is', 'immutable']
'String is immutable'.split(' ',1)
                             
['String', 'is immutable']
s='''
python
programming
language'''
                             
s
                             
'\npython\nprogramming\nlanguage'
s.splitlines()
                             
['', 'python', 'programming', 'language']
''.join(['', 'python', 'programming', 'language'])
                             
'pythonprogramminglanguage'
' '.join(['', 'python', 'programming', 'language'])
                             
' python programming language'
'-'.join(['', 'python', 'programming', 'language'])
                             
'-python-programming-language'
>>> ','.join(['1','2','3'])
...                              
'1,2,3'
>>> 'python.py'.partition('.')
...                              
('python', '.', 'py')
>>> s='java,python,c,c++'
...                              
>>> s.partition(',')
...                              
('java', ',', 'python,c,c++')
>>> s.rpartition(',')
...                              
('java,python,c', ',', 'c++')
>>> c='                  Hello                world                '
...                              
>>> c
...                              
'                  Hello                world                '
>>> c.strip()
...                              
'Hello                world'
>>> c.lstrip()
...                              
'Hello                world                '
>>> c.rstrip()
...                              
'                  Hello                world'
>>> text="Hello 🙂"
...                              
>>> text.encode()
...                              
b'Hello \xf0\x9f\x99\x82'
>>> b'Hello \xf0\x9f\x99\x82'.decode()
...                              
'Hello 🙂'
