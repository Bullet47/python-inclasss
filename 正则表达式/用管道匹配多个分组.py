import re

'''
字符|称为“管道”。希望匹配许多表达式中的一个时，就可以使用它。例如，
正则表达式r'Batman|Tina Fey'将匹配'Batman'或'Tina Fey'。
如果 Batman 和Tina Fey 都出现在被查找的字符串中，第一次出现的匹配文本，
将作为Match 对象返回。在交互式环境中输入以下代码：
'''
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
'''
假设你希望匹配'Batman'、'Batmobile'、'Batcopter'和'Batbat'中任意一个。因为所有这
些字符串都以Bat 开始，所以如果能够只指定一次前缀，就很方便。这可以通过括
号实现。在交互式环境中输入以下代码：
'''
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
