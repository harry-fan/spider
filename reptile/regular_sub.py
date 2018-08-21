
import re


p = re.compile(r'(?P<word1>\w+) (?P<word2>\w+)')
s = 'i say, hello world!'
print(p.sub(r'\g<word2> \g<word1>', s))

p = re.compile(r'(\w+) (\w+)')
print(p.sub(r'\2 \1', s))

def func(m):
    #print(type(m))
    return m.group(1).title() + ' ' + m.group(2).title()

print(p.sub(func, s))
#print(s.group(1).title())
#print(s.group(2).title())

p = re.compile(r'(\w+) (\w+)')
print(p.subn(r'\2 \1', s))
print('='*50)
print(p.subn(func, s))
