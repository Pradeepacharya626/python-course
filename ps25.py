            #DAY 7

#to convert 1.doc to 1-doc.txt

filenames = ["1.doc","2.report","3.presentation"]
filenames = [filename.replace('.','-')+"txt" for filename in filenames]
print(filenames)