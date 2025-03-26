#데이터 채우기

import openpyxl as excel

book = excel.Workbook()

sheet = book.active

for i in range(10):
    row_cell = sheet.cell(row=(i+1), column=1) # 행과 열 지정하기 
    row_cell.value = str(i+1) + " 번째 데이터 저장"

book.save("py_excel01.xlsx")