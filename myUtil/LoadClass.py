import os
import xlwt

_PATH = "/Users/penggao/IdeaProjects/dx-web/src/main/java/com/redhorse/web/"
_RESULT = []
_TARGET_EXCEL_PATH = '/Users/penggao/Desktop/1.xls'

def load_java(filePath):
    key = '  @RequestMapping('
    f = open(filePath)
    line = f.readline()
    while line:
        if key in line:
            print(line)
            _RESULT.append(line)
        line = f.readline()
    f.close()

# 设置表格样式
def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


# 写Excel
def write_excel():
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('学生', cell_overwrite_ok=True)
    row0 = ["姓名", "年龄", "出生日期", "爱好"]
    colum0 = _RESULT
    # 写第一行
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))
    # 写第一列
    for i in range(0, len(colum0)):
        sheet1.write(i + 1, 0, colum0[i], set_style('Times New Roman', 220, True))

    # sheet1.write(1, 3, '2006/12/12')
    # sheet1.write_merge(6, 6, 1, 3, '未知')  # 合并行单元格
    # sheet1.write_merge(1, 2, 3, 3, '打游戏')  # 合并列单元格
    # sheet1.write_merge(4, 5, 3, 3, '打篮球')

    f.save(_TARGET_EXCEL_PATH)


if __name__ == '__main__':
    files = os.listdir(_PATH)
    for f in files:
        print('----------- ' + f + '---------------')
        _RESULT.append('----------- ' + f + '---------------')
        filePath = _PATH + f
        # print(filePath)
        load_java(filePath)

    write_excel()
