'''处理FileNotFoundError 异常'''
'''使用文件时，一种常见的问题是找不到文件：你要查找的文件可能在其他地方、文件名可能不正确或者这个文件根本就不存在。
对于所有这些情形，都可使用try-except 代码
块以直观的方式进行处理。'''
filename = 'alice.txt'
try:
    # with open(filename) as f_obj:
    #     contents = f_obj.read()
    a = 5 / 0
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
except ZeroDivisionError:
    msg = "Sorry, the file " + filename + " does not exist sad asd ."
    print(msg)
'''
异常的参数
'''


# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:  # 将捕获到的异常对象赋值给Argument
        print("参数没有包含数字\n" + str(Argument))  # str(Argument)将会输出错误信息

# 调用函数
temp_convert("xyz")
