def genCode(names, remarks):
    nameList = names.split(",")
    remarksList = remarks.split(",")

    tempalte = ''

    i = 0
    num = 0
    for name in nameList:
        num = num + 1
        tempalte = tempalte + '/**\n* ' + remarksList[
            i] + '\n*/' + '\npublic static final String ' + name + ' = "' + str(num) + '";\n'
        i = i + 1

    return tempalte


str1 = "1:月度达人红包,2:季度京东E卡,3:季度乐享大礼包,4:季度升段祝福,5:年度健康关爱大礼包,6:年度尊享,7:年度全国双飞,8:年度8888现金红包,9:年度与CEO共进晚餐'"
str2 = "REWARD_1,REWARD_2,REWARD_3,REWARD_4,REWARD_5,REWARD_6,REWARD_7,REWARD_8,REWARD_9"
print(genCode(str2, str1))
