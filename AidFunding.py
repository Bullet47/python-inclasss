def aid(income, children_num):
    fund = 0
    if 30000 <= income < 40000 and children_num >= 3:
        fund = 1000 * children_num
    elif 20000 <= income < 30000 and children_num >= 2:
        fund = 1500 * children_num
    elif income < 20000:
        fund = 2000 * children_num
    return fund


if __name__ == '__main__':
    while True:
        print("欢迎进入援助资金查询系统")
        print("1.查询援助资金")
        print("2.退出查询系统")
        print("请输入功能选项")
        select = int(input())
        if select == 1:
            income = int(input("请输入家庭年收入(美元) "))
            children_num = int(input("请输入孩子数量 "))
            print("援助资金应为：" + str(aid(income, children_num)) + "美元")
        else:
            print("已退出查询系统")
            break
