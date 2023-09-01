            #DAY 13

#modification in ps40.py

# 1st one

feet_inches = input("enter value for feet and inches")

def feetinches(feet_inch):
  parts = feet_inch.split(" ")
  feet = float(parts[0])
  inches = float(parts[1])
  meters = feet*0.3048 +inches*0.0254
  return feet,inches,meters


parts = feetinches(feet_inches)
print(f"{parts[0]}feet, {parts[1]}inches is equal to {parts[2]}meters")


# 2nd

feet_inches = input("enter value for feet and inches")

def feetinches(feet_inch):
  parts = feet_inch.split(" ")
  feet = float(parts[0])
  inches = float(parts[1])
  return feet, inches

def convert(feet,inches) :
  meters = feet*0.3048 +inches*0.0254
  return meters

parts = feetinches(feet_inches)
result = convert(parts[0],parts[1])
print(f"{parts[0]}feet,{parts[1]}inches is equal to {result}meters")

#bye