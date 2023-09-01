        #DAY 3

todos = []

while True :
  user = input("Type add,show or exit")
  user = user.strip()      # used to convert "add " to "add"
  match user :
    case 'add' :
      todo = input("Enter a todo")
      todos.append(todo)
    case 'show' :
      for item in todos:
          print(item)
    case 'exit' :
      break

print("Bye")