def genCode(names, remarks):
    nameList = names.split(",")
    remarksList = remarks.split(",")

    tempalte = ''

    i = 0
    for name in nameList:
        tempalte = tempalte + '/**\n* ' + remarksList[i] + '\n*/' + '\nprivate String ' + name + ' = "";\n'
        i = i + 1

    return tempalte
