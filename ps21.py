        #DAY 6

#writing Hai in all the text files

filenames = ["doc.txt","report.txt","presentation.txt"]
for filename in filenames :
  file = open(f"pradeep/{filename}",'w')
  file.writelines("Hai")
  file.close()