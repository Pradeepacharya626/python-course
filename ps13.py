          #DAY 5

# TO SORT THE LIST IN ASCENDING ORDER
my_list = ["john","ben","lisa"]
my_list.sort()
# my_list.sort(reverse=False)   # - this is also used for ascend
for index,item in enumerate(my_list) :
  print(f"{index+1}-{item.capitalize()}")

#TO SORT THE LIST IN DESCENDING ORDER
my_list = ["john","ben","lisa"]
my_list.sort(reverse=True)
for index,item in enumerate(my_list) :
  print(f"{index+1}-{item.capitalize()}")