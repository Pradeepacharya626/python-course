        #DAY 4

todos = []

while True :
  user = input("Type add,show,edit or exit")
  user = user.strip()      # used to convert "add " to "add"
  match user :
    case 'add' :
      todo = input("Enter a todo")
      todos.append(todo)
    case 'edit' :
      number = int(input("Enter the number"))
      print(todos[number])
      msg = input("enter something")
      todos[number] = msg
      print(todos[number])
      print(todos)
    case 'show' :
      for item in todos:
          print(item)
    case 'exit' :
      break

print("Bye")