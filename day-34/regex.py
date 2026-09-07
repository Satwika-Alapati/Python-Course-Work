'''
import re

pattern=r'[0-9]'
text='codegnan'

res=re.match(pattern,text)

print(res.group() if res else "Pattern not found")
'''




'''
import re

pattern=r'[0-9]'
text='codegnan2026'

res=re.search(pattern,text)

print(res.group() if res else "Pattern not found")

'''


'''
import re

pattern=r'[0-9]'
text='codegnan 2026 python version 3.14 '

res=re.findall(pattern,text)

print(res)

#print(res.group() if res else "Pattern not found")
'''

'''
import re

pattern=r'[0-9]'
text='codegnan 2026 python version 3.14 '

res=re.finditer(pattern,text)

for i in res:
    print(i.group(),i.start())

#print(res.group() if res else "Pattern not found")
'''




'''
import re

pattern=r'[0-9]{16}'
text='9876543210'

res=re.fullmatch(pattern,text)

print(res)

#print(res.group() if res else "Pattern not found")
'''



'''
import re

pattern=r'[,(#)]'
text='java,python(html#css '

res=re.split(pattern,text)

print(res)

#print(res.group() if res else "Pattern not found")
'''


'''
import re

pattern=r'[a-z]'
text='python version 3.14,batch-63 '

res=re.sub(pattern,'*',text)

print(res)

#print(res.group() if res else "Pattern not found")
'''


'''
import re

pattern=r'e.t'
text='e@t eaat eat eet ett ect Egfhjet hgjeokj '

res=re.findall(pattern,text)

print(res)

#print(res.group() if res else "Pattern not found")
'''




'''
import re

pattern=r'^91'
text='919876543210'

res=re.findall(pattern,text)

print(res)

#print(res.group() if res else "Pattern not found")

'''


'''
import re

pattern=r'0$'
text='919876543210'

res=re.findall(pattern,text)

print(res)

#print(res.group() if res else "Pattern not found")
'''

'''
import re

pattern=r'to+'
text='to tdfghjk too tooo tooooooo'

res=re.findall(pattern,text)

print(res)

#print(res.group() if res else "Pattern not found")
'''

'''
import re

pattern=r'([a-zA-Z])*'
text='Codegnan Programming'

res=re.findall(pattern,text)

print(res)

#print(res.group() if res else "Pattern not found")
'''

'''
import re

pattern=r'ab+'
text='ab abbb a abbbbbb abbbb'

res=re.findall(pattern,text)

print(res)

#print(res.group() if res else "Pattern not found")
'''



'''
import re

pattern=r't?o'
text='t t@ooo tso td th tu'

res=re.findall(pattern,text)

print(res)

#print(res.group() if res else "Pattern not found")
'''




'''
import re

pattern=r'colo?rs'
text='colours'

res=re.findall(pattern,text)

print(res)

#print(res.group() if res else "Pattern not found")
'''




'''
import re

pattern=r'91|0'
text='05678'

res=re.findall(pattern,text)

print(res)

#print(res.group() if res else "Pattern not found")
'''



import re

pattern=r'[aeiouAEIOU]'
text='codegnan programming'

res=re.findall(pattern,text)

print(res)

#print(res.group() if res else "Pattern not found")