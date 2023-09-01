
              #DAY 11

# to find average

def get_average():
  with open(".config/ps2.txt",'r') as file :
    values = file.readlines()
    data = values[1:]
    value = [float(i) for i in data]
  return value

new_average = get_average()

average = sum(new_average)/len(new_average)

print(average)