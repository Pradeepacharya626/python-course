# CALCULATOR

# import hashlib
# a=input("enter the value of a")
# b=input("enter the value of b")
# a=5
# b=3
# print("the value of ",a," + ",b,"is :",a+b)
# print("the value of ",a," - ",b,"is :",a-b)
# print("the value of ",a," / ",b,"is :",a/b)
# print("the value of ",a," // ",b,"is :",a//b)



# CALCULATOR 2

num1 = float(input("Enter the value of 1st number"))
num2 = float(input("Enter the value of 2nd number"))
print("1.Addition\n2.Subtraction\n3.multiplication\n4.Division\n")
choice = int(input("Enter the choice b/n "1" to 4"))
if choice==1 :
  print("Addition=",num1+num2)
elif choice==2 :
  print("Subtraction=",num1-num2)
elif choice==3 :
  print("Multiplication=",num1*num2)
elif choice==4 :
  print("Division")
else :
  print("Invalid choice")

