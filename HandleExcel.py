#encoding=utf8

from __future__ import print_function
import xlrd

data = xlrd.open_workbook('Latest.xlsx')
#table = data.sheets()[0] #通过索引获取工作表
#table = data.sheet_by_index(0) #通过索引顺序获取
table = data.sheet_by_name(u'Sheet1') #通过名称获取
#获取整行和整列的值
#table.row_values(i)
#table.col_values(i)

#获取行数和列数
nrows = table.nrows
ncols = table.ncols
list_dispose = []
for k, v in enumerate(table.col_values(0)):
  if v.startswith('@') or v.startswith(' @'):
    list_dispose.append(v)

count = 0
#f = open("domain1.txt", 'wb')
for exactone in list_dispose:
  #f.write(exactone)
  print(exactone,end = ' ')
  count+=1
  if (count%5) == 0:
    print(end = '\n')

#for i in list_dispose:
#  print(i, end=' ')
#  count += 1
#  if(count%5==0)
#    print(end='\n')
#    print("", file = f)

#可以在命令行中用如下命令来将打印结果导入到textfile.txt
#python myawesomescript.py >> textfile.txt

print(ncols)
print(nrows)