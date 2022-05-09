class bad(Exception):
    pass


def doommed():
    raise bad()


try:
    doommed()
except  bad as e:
    print('得到自定义异常' + str(e))
