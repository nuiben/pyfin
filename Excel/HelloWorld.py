from openpyxl import Workbook

filename = "hello_world.xlsx"

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world!"

workbook.save(filename=filename)
