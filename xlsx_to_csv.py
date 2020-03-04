import xlrd
import csv
from datetime import datetime

xl_file = "TestFile\Sample.xlsx"

workbook = xlrd.open_workbook(xl_file)

sheet = workbook.sheets()[0]

csvname = "TestFile\Converted.csv"
cf = open(csvname, "w", newline='\n')
cw = csv.writer(cf)

for r in range(0, sheet.nrows):
    row = []
    for cell in sheet.row(r):
        if isinstance(cell.value, float):
            row.append(datetime(*xlrd.xldate_as_tuple(cell.value, 0)).strftime('%d/%m/%Y'))
        else:
            row.append(cell.value)
    cw.writerow(row)

workbook.release_resources()
del workbook
cf.close()