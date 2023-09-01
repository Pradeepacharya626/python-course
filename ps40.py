            #DAY 12

'''feet_inches = input("Enter value of feet and inches")
parts = feet_inches.split(" ")
feet = float(parts[0])
inches = float(parts[1])
meters = feet*0.3048 + inches*0.0254
print(f"{feet} feet,{inches}inches equal to {meters} meters")'''

# above program using def function

feet_inches = input("enter value for feet and inches")



def convert(feet_inch) :
  parts = feet_inch.split(" ")
  feet = float(parts[0])
  inches = float(parts[1])
  meters = feet*0.3048 +inches*0.0254
  return f"{feet} feet,{inches}inches equal to {meters} meters"


print(convert(feet_inches))