import re

'''
假定想要将区号从电话号码中分离。添加括号将在正则表达式中创建“分组”：
(\d\d\d)-(\d\d\d-\d\d\d\d)。然后可以使用group()匹配对象方法，从一个分组中获取匹
配的文本。
正则表达式字符串中的第一对括号是第1 组。第二对括号是第2 组。向group()
匹配对象方法传入整数1 或2，就可以取得匹配文本的不同部分。向group()方法传
入0 或不传入参数，将返回整个匹配的文本。
'''
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')


# 括号在正则表达式中有特殊的含义，但是如果你需要在文本中匹配括号，怎么
# 办？例如，你要匹配的电话号码，可能将区号放在一对括号中。在这种情况下，就
# 需要用倒斜杠对(和)进行字符转义。在交互式环境中输入以下代码：
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))
#mo.group(2)
#传递给re.compile()的原始字符串中，\(和\)转义字符将匹配实际的括号字符。
