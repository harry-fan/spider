import re

#正则表达式编译成pattern对象
pattern = re.compile(r'\d+')

#使用re.match(pattern, '')匹配文本，获取匹配结果
result = re.match(pattern, '192abc')
if result:
    print(result.group())
else:
    print('error')

result2 = re.match(pattern, 'abc192')
if result2:
    print(result2.group())
else:
    print('error two')
