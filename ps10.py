          # DAY 4

# mylist = ['a','b','c',5]
# print(mylist.index(5))
# print(mylist.index('b'))


'''.replace() function is used to replace'''
filenames = ["1.Raw Data.txt","2.reports.txt","3.presentation .txt"]
for filename in filenames :
  filename = filename.replace('.','-')
  print(filename)
for filename in filenames :
  filename = filename.replace('.','-',1)  #to replace 1st . of every str
  print(filename)
