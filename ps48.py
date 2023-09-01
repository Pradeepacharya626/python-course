                      #DAY 15

#glob module

import glob                     

myfiles = glob.glob("*.txt")    #glob is a function used to list all txt files and we can also write like this "myfiles = glob.glob("*.py")" to get .py files

print(myfiles)

for filepath in myfiles :
  with open(filepath,'r') as file :
    print(file.read())


'''if u want to list the files from another directory, use
    myfiles = glob.glob("pradeep/pradi/*.txt")'''