            #DAY 8

# percentage of head or tail by using with-context manager

while True :
  with open("file.txt","r") as file :
    sides = file.readlines()

  side = input("Throw the coin and enter head or tail here?") + "\n"

  sides.append(side)

  with open("file.txt","w") as file :
    file.writelines(sides)

  head_count = sides.count("head\n")   # becoz list contain 1st \n
  percentage = (head_count/len(sides))*100

  print(f"Head : {percentage}%")

  