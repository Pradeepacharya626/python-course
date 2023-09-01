        #DAY 2

msg = "Enter a todo"
while True :
  todo = input(msg)
  print(todo)

"""True is a boolian . if we write the condition as True, it is always true and loop continues for infinit times...
if we write False as a condition ,it is false and hence control doesnotnenter the loop"""

# msg = "Enter a todo"
# while False :
#   todo = input(msg)
#   print(todo)

msg = "Enter a todo"

todos = []

while True :
  todo = input(msg)
  todos.append(todo)    #FUNTION IS USED TO ADD INPUT TO LIST
  print(todos)
  