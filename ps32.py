            #DAY 9

# modify of ps31.py by using "DICTIONARY"

password = input("Enter password")

results = {}

if len(password) >= 8 :
  results["length"] = True
else :
  results["length"] = False

digit = False
for i in password :
  if i.isdigit() :
    digit = True
    

results["digit"] = digit

upper_case = False
for i in password :
  if i.isupper():
    upper_case = True

results["uppercase"] = upper_case

if all(results.values()) :
  print("Strong password")
else :
  print("Weak password")
  