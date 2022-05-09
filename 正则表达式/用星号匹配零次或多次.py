import re
'''
*（称为星号）意味着“匹配零次或多次”，即星号之前的分组，可以在文本中出
现任意次。它可以完全不存在，或一次又一次地重复。让我们再来看看Batman 的例子。
如果需要匹配真正的星号字符，就在正则表达式的星号字符前加上倒斜杠，即\*。
'''
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
#'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
#'Batwoman'
mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
#'Batwowowowoman'
'''
对于'Batman'，正则表达式的(wo)*部分匹配wo 的零个实例。对于'Batwoman'，
(wo)*匹配wo 的一个实例。对于'Batwowowowoman'，(wo)*匹配wo 的4 个实例。
'''
'''用加号匹配一次或多次 e.g. batRegex = re.compile(r'Bat(wo)+man')
用花括号匹配特定次数  haRegex = re.compile(r'(Ha){3}')
'''