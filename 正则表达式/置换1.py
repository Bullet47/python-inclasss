import random

az_list = [chr(i) for i in range(97, 123)]  # 小写字母表
AZ_list = [chr(i) for i in range(65, 91)]  # 大写字母表
random_list = az_list + AZ_list
random.shuffle(random_list)  # 打乱字母表
origin_alphabet_list = az_list + AZ_list  # 原始字母表顺序
dict_decode = {}  # 加密字典
dict_encode = {}  # 解密字典
for i in range(0, len(origin_alphabet_list)):
    dict_decode[origin_alphabet_list[i]] = random_list[i]  # 生成加密字典中的键值对


def decode(list_str):  # 加密
    for i in range(0, len(list_str)):
        if ascii('a') <= ascii(list_str[i]) <= ascii('z') or ascii('A') <= ascii(list_str[i]) <= ascii('Z'):
            dict_encode[dict_decode[list_str[i]]] = list_str[i]
            list_str[i] = dict_decode[list_str[i]]  # 反向记录每一个键值对
    return list_str


def encode(list_str):
    for i in range(0, len(list_str)):
        if ascii('a') <= ascii(list_str[i]) <= ascii('z') or ascii('A') <= ascii(list_str[i]) <= ascii('Z'):
            list_str[i] = dict_encode[list_str[i]]  # 解密
    return list_str


if __name__ == '__main__':
    str = "Five score years ago, a great American, in whose symbolic shadow we stand today, signed the Emancipation " \
          "Proclamation. This momentous decree came as a great beacon light of hope to millions of Negro slaves who " \
          "had been seared in the flames of withering injustice. It came as a joyous daybreak to end the long night " \
          "of bad captivity. "
    print("原始串：\n" + str)
    list_str = list(str)  # 先将字符串转换为列表
    list_decode_str = decode(list_str)
    decode_str = "".join(list_decode_str)  # 将列表转为字符串
    print("加密后：\n" + decode_str)
    list_encode_str = encode(list_decode_str)
    encode_str = "".join(list_encode_str)  # 将列表转为字符串
    print("解密后：\n" + encode_str)
