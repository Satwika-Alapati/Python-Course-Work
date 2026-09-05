Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
9/2
4.5
a//b
2
9//2
4
9%2
1
3**2
9
4**2
16
a
20
b
10
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
c=10
c+=10
c
20
c+=10
c
30
c-=10
c
20
c*=2
c
40
c//=2
c
20
c**=2
c
400
c%=3
c
1
c/=2
c
0.5
True and True
True
n=10
n%2==0
True
n%3==0
False
n%2==0 and n%3==0
False
n%2==0 or n%3==0
True
n%8==0 or n%3==0
False
n
10
n<5
False
not n<5
True
#str list tuple set dict
s='codegnan'
'e' in s
True
'z' in s
False
'f' not in s
True
'o' not in s
False
l=[1,2,3,4]
4 in l
True
6 in l
False
8 not in l
True
t=(1,2,3,4)
1 in t
True
5 not in t
True
s={1,2,3,4,5,6,7}
6 in s
True
8 not in s
True
d={'name':'jack','batch':63,'course':'pfs'}
'name' in d
True
'jack' in d
False
63 in d
False
'pfs' in d
False
'batch' in d
True
'age' not in d
True
l=[1,2,3,4]
m=[1,2,3,4]
id(l)
2579305198720
id(m)
2579305198656
l is m
False
n=l
id(n)
2579305198720
l is n
True
l is not m
True
l is not n
False
s='codegnan'
id(s)
2579305414768
s='codegnan course'
s
'codegnan course'
id(s)
2579305418160
a=10
id(a)
140703709018840
a+=10
a
20
id(a)
140703709019160
s={1,2,3,4}
id(s)
2579300299744
s.add(5)
s
{1, 2, 3, 4, 5}
id(s)
2579300299744
d={'name':'jack','batch':63,'course':'pfs'}
id(d)
2579305374080
d['age']=20
d
{'name': 'jack', 'batch': 63, 'course': 'pfs', 'age': 20}
id(d)
2579305374080
l=[1,2,3,4]
id(l)
2579261412096
l.append(6)
l
[1, 2, 3, 4, 6]
id(l)
2579261412096
9&10
8
9|10
11
9^10
3
8>>2
2
8<<2
32
8>>3
1
~8
-9
12
12
~12
-13
~45
-46
a=10
b=10.3
c='codegnan'
>>> print(a,b,c)
10 10.3 codegnan
>>> print("a value is",a)
a value is 10
>>> print("a value is",a,"b value is",b,"c value is",c)
a value is 10 b value is 10.3 c value is codegnan
>>> print("a value is",a,|"b value is",b,|"c value is",c)
SyntaxError: invalid syntax
>>> print("a value is",a,"|b value is",b,"|c value is",c)
a value is 10 |b value is 10.3 |c value is codegnan
>>> print(a,b,c)
10 10.3 codegnan
>>> print(a,b,c,sep='')
1010.3codegnan
>>> print(a,b,c,sep='\n')
10
10.3
codegnan
>>> print(a,b,c,sep='\t')
10	10.3	codegnan
>>> print(a,b,c,sep='\t',end='@')
10	10.3	codegnan@
>>> print(a,b,c,sep='\t',end='\n\n')
10	10.3	codegnan

>>> print(f'a={a} b={b} c={c}')
a=10 b=10.3 c=codegnan
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=10.300000 c=codegnan
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
a=10 b=10.30 c=codegnan
>>> print('a={}|b={}|c={}'.format(a,b,c))
a=10|b=10.3|c=codegnan
>>> print('a={}|b={}|c={}'.format(c,a,b))
a=codegnan|b=10|c=10.3
>>> print('a={1}|b={2}|c={0}'.format(a,b,c))
a=10.3|b=codegnan|c=10
