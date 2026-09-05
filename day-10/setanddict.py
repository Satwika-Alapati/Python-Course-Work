Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
data={'name':'satwika','batch':63,'couse':'PFS'}
data['name']
'satwika'
data['batch']
63
data['couse']
'PFS'
63 in data
False
data['age']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('age','key is not present')
'key is not present'
data.get('couse','key is not present')
'PFS'
data['batch']=64
data
{'name': 'satwika', 'batch': 64, 'couse': 'PFS'}
data['skills']=['python','mysql','flask']
data
{'name': 'satwika', 'batch': 64, 'couse': 'PFS', 'skills': ['python', 'mysql', 'flask']}
data['age']=21
data
{'name': 'satwika', 'batch': 64, 'couse': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21}
data.update({'phno':987456123,'email':'satwika@gmail.com'})
data
{'name': 'satwika', 'batch': 64, 'couse': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 987456123, 'email': 'satwika@gmail.com'}
data.pop('age')
21
data
{'name': 'satwika', 'batch': 64, 'couse': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 987456123, 'email': 'satwika@gmail.com'}
data.pop('phno')
987456123
data
{'name': 'satwika', 'batch': 64, 'couse': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'email': 'satwika@gmail.com'}
del data['name']
data
{'batch': 64, 'couse': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'email': 'satwika@gmail.com'}
data.popitem()
('email', 'satwika@gmail.com')
data
{'batch': 64, 'couse': 'PFS', 'skills': ['python', 'mysql', 'flask']}
data.popitem()
('skills', ['python', 'mysql', 'flask'])
data
{'batch': 64, 'couse': 'PFS'}
data.clear()
data
{}
data
{}
data={'name': 'satwika', 'batch': 64, 'couse': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 987456123, 'email': 'satwika@gmail.com'}
data
{'name': 'satwika', 'batch': 64, 'couse': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 987456123, 'email': 'satwika@gmail.com'}
data.keys()
dict_keys(['name', 'batch', 'couse', 'skills', 'age', 'phno', 'email'])
data.values()
dict_values(['satwika', 64, 'PFS', ['python', 'mysql', 'flask'], 21, 987456123, 'satwika@gmail.com'])
data.items()
dict_items([('name', 'satwika'), ('batch', 64), ('couse', 'PFS'), ('skills', ['python', 'mysql', 'flask']), ('age', 21), ('phno', 987456123), ('email', 'satwika@gmail.com')])
sorted(data)
['age', 'batch', 'couse', 'email', 'name', 'phno', 'skills']
sorted(data,reverse=True)
['skills', 'phno', 'name', 'email', 'couse', 'batch', 'age']
max(data)
'skills'
min(data)
'age'
data
{'name': 'satwika', 'batch': 64, 'couse': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 987456123, 'email': 'satwika@gmail.com'}
data['password']
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    data['password']
KeyError: 'password'
data.get('password')
>>> data.setdefault('password',0)
0
>>> data
{'name': 'satwika', 'batch': 64, 'couse': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 987456123, 'email': 'satwika@gmail.com', 'password': 0}
>>> data.setdefault('name','')
'satwika'
>>> data
{'name': 'satwika', 'batch': 64, 'couse': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 987456123, 'email': 'satwika@gmail.com', 'password': 0}
>>> len(data)
8
>>> all(data)
True
>>> any(data)
True
>>> data
{'name': 'satwika', 'batch': 64, 'couse': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 987456123, 'email': 'satwika@gmail.com', 'password': 0}
>>> a
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a={1:1,2:2}
>>> b=a
>>> b
{1: 1, 2: 2}
>>> c=a.copy()
>>> c[4]=4
>>> c
{1: 1, 2: 2, 4: 4}
>>> a
{1: 1, 2: 2}
>>> d=dict.fromkeys(["a","b"],0)
>>> d
{'a': 0, 'b': 0}
