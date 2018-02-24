import pandas as pd


def readExcel():
    xl = pd.ExcelFile('/pythonGP1/1.xls')
    df1 = xl.parse('Sheet1')
    return df1
