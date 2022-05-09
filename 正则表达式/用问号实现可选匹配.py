import re
'''
有时候，想匹配的模式是可选的。就是说，不论这段文本在不在，正则表达式
都会认为匹配。字符?表明它前面的分组在这个模式中是可选的。例如，在交互式
环境中输入以下代码：
'''
# 如果需要匹配真正的问号字符，就使用转义字符\?。
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
# 正则表达式中的(wo)?部分表明，模式wo 是可选的分组。该正则表达式匹配的文本
# 中，wo 将出现零次或一次。这就是为什么正则表达式既匹配'Batwoman'，又匹配'Batman'。