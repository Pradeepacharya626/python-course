        #DAY 3

todos = []

while True :
  user = input("Type add,show or exit")
  match user :
    case 'add' :
      todo = input("Enter a todo")
      todos.append(todo)
    case 'show' :
      print(todos)
    case 'exit' :
      break

print("Bye")