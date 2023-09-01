            #DAY 8

# percentage of head or tail

sides = []

while True :
  side = input("Through the coin and enter head or tail here?")
  sides.append(side)
  head_count = sides.count("head")
  percentage = (head_count/len(sides))*100
  print(f"Head : {percentage}%")