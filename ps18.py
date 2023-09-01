
#DAY 6

#to creat a file and add content to that file

contents = ["life is full of surprices and miracles",
            "sometimes life fucks",
            "sometimes we fuck"]
filenames = ["doc.txt","report.txt","presentation.txt"]
for content,filename in zip(contents,filenames) :
  file  = open(f"pradeep/pradi/{filename}",'w')
  file.writelines(content)
file.close()
  
  