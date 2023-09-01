            #DAY 9

password = input("Enter password")

results = []

if len(password) >= 8 :
  results.append(True)
else :
  results.append(False)

digit = False
for i in password :
  if i.isdigit() :
    digit = True

results.append(digit)

upper_case = False
for i in password :
  if i.isupper():
    upper_case = True

results.append(upper_case)

if all(results) : #also can be written that if all(results) == True :
  print("Strong password")
else :
  print("Weak password")
  