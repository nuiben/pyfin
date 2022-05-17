import openpyxl
import os

os.chdir('.\\pyfin\\Excel')
wb = openpyxl.load_workbook(
    '.\\pyfin\\Excel\\example.xlsx')

type(wb)
