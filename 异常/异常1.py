#处理ZeroDivisionError异常
# print(5/0)
# ZeroDivisionError: division by zero
'''
使用try-except 代码块
当你认为可能发生了错误时，可编写一个try-except 代码块来处理可能引发的异常。你让Python尝试运行一些代码，并告诉它如果这些代码引发了指定的异常，该怎么办。
处理ZeroDivisionError 异常的try-except 代码块类似于下面这样：
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("你不能用0作除数")
'''
我们将导致错误的代码行print(5/0) 放在了一个try 代码块中。如果try 代码块中的代码运行起来没有问题，Python将跳过except 代码块；如果try 代码块中的代码导致了
错误，Python将查找这样的except 代码块，并运行其中的代码，即其中指定的错误与引发的错误相同。
 else 代码块
 通过将可能引发错误的代码放在try-except 代码块中，可提高这个程序抵御错误的能力。错误是执行除法运算的代码行导致的，因此我们需要将它放到try-except 代码块
中。
这个示例还包含一个else 代码块；依赖于try 代码块成功执行的代码都应放到else 代码块中：
 '''
try:
    answer = int(first_number) / int(second_number)
except ZeroDivisionError:
    print("You can't divide by 0!")
except Exception as e:
    print("执行到Exception")
    print(str(e))
else:
    print(answer)
finally:
    print("无论有没有错误都会最后执行finally语句块")
'''
except 代码块告诉Python，出现ZeroDivisionError 异常时该怎么办（见❷）。如果try 代码块因除零错误而失败，我们就打印一条友好的消息，告诉用户如何避免这种错
误。程序将继续运行，用户根本看不到traceback：
'''