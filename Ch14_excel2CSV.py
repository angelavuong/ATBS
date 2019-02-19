import openpyxl
import csv
import os


files = os.listdir('/Users/angvuong/atbs/excelSpreadsheets')
for file in files:
    if '.csv' in file:
        newfile = file.replace('.csv', '.xlsx')
        os.rename(file, newfile)
