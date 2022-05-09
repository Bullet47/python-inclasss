profit = float(input("请输入利润（单位：万）："))
bonus = 0
if profit <= 10:  # 小于等于10
    bonus = profit * 0.1
elif (profit > 10) and (profit <= 20):  # 大于10小于等于20
    bonus = 10 * 0.1 + (profit - 10) * 0.075
elif (profit > 20) and (profit <= 40):  # 大于20小于等于40
    bonus = 10 * 0.1 + 10 * 0.075 + (profit - 20) * 0.05
elif (profit > 40) and (profit <= 60):  # 大于40小于等于60
    bonus = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (profit - 40) * 0.03
elif (profit > 60) and (profit <= 100):  # 大于60小于等于100
    bonus = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (profit - 60) * 0.015
elif profit > 100:  # 大于100
    bonus = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (profit - 100) * 0.01
print("奖金数目为 " + str(bonus) + "万")
