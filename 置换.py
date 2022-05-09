# translate()函数也是python自带。与replace() 函数不同的是，
# 这里使用str.maketrans函数来创建一个表，它可以使用各种参数，但是需要三个Arguments。
import random

az_list = []
AZ_list = []
alphabet_list = []  # 字母表
for i in range(0, 26):
    az_list.append(chr(i + 97))  # 小写
    AZ_list.append(chr(i + 65))
alphabet_list = az_list + AZ_list
random.shuffle(alphabet_list)
origin_alphabet_list = az_list + AZ_list
intab = "".join(origin_alphabet_list)
# print(intab)
outtab = ''.join(alphabet_list)
# print(outtab)
trantab1 = str.maketrans(intab, outtab)
trantab2 = str.maketrans(outtab, intab)


def decode(str):
    str = str.translate(trantab1)
    return str


def encode(str):
    str = str.translate(trantab2)
    return str


if __name__ == '__main__':
    str = "asdasdadqwqweASDASDASDASD"
    print(str)
    Encrypted_str = decode(str)
    print(Encrypted_str)
    Decrypted_str = encode(Encrypted_str)
    print(Decrypted_str)
