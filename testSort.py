def insert_sort(ary):
    n = len (ary)
    for i in range (1, n):  # 从第二个元素提取数据，遍历比较
        temp = ary[i]
        index = i  # 待插入的下标
        for j in range (i - 1, -1, -1):  # 从i-1 循环到 0 (包括0)
            if ary[j] > temp:  # 判断当前元素是否小于此位置的数值
                ary[j + 1] = ary[j]  # 移动元素到后面
                index = j  # 记录空闲位置
            else:
                break
        ary[index] = temp  # 数值插入到此位置
    return ary


num = 0;


def bubble_sort(arry):
    n = len (arry)  # 获得数组的长度

    for i in range (n):  # 从头开始遍历数组
        for j in range (1, n - i):  # 每次便利后，最后i个元素肯定就比较完大小
            # global num
            # num = num + 1
            if arry[j - 1] > arry[j]:  # 临近的2个元素比较，
                arry[j - 1], arry[j] = arry[j], arry[j - 1]  # 如果前一个元素大，则交换两者
    return arry


def select_sort(ary):
    n = len (ary)
    for i in range (0, n):
        min = i  # 最小元素下标标记s
        for j in range (i + 1, n):
            # global num
            # num = num + 1
            if ary[j] < ary[min]:
                min = j  # 找到最小值的下标
        ary[min], ary[i] = ary[i], ary[min]  # 交换两者
    return ary


l = [5, 4, 3, 21, 1, 3, 4, 3, 323424, 10]
print (select_sort (l))
print ('执行了次数：' + str (num))
