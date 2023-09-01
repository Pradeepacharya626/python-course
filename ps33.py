            #DAY 10

length = float(input("Enter value for length"))
width = float(input("Enter the value for width"))

perimeter = (length + width) *2
area = length*width

print("perimeter is :",perimeter)
print("area is :",area)

if perimeter >14 and area > 8 :
  print("OK")
else :
  print("NOT OK")