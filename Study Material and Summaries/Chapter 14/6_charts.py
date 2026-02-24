# CHAPTER 14 - SECTION 6: CHARTS

# What: Create charts (bar, line, pie) in Excel from data
# Why: Visualize data instead of just numbers
# How: Create Reference, Series, and Chart objects, then add to sheet

import openpyxl
from openpyxl.chart import Reference, Series, BarChart

wb = openpyxl.Workbook()
sheet = wb.active

# Add data
for i in range(1, 11):
    sheet['A' + str(i)] = i

# Create a Reference object for cells
refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)

# Create a Series object
seriesObj = openpyxl.chart.Series(refObj, title='First series')

# Create a Chart object
chartObj = openpyxl.chart.BarChart()
chartObj.title = 'My Chart'
chartObj.append(seriesObj)

# Add chart to the sheet
sheet.add_chart(chartObj, 'C5')

wb.save('sampleChart.xlsx')
