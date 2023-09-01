              #DAY 5

      #ENUMERATE AND f STRING

todos = []

while True :
  user = input("Type add,show or exit")
  user = user.strip()      # used to convert "add " to "add"
  match user :
    case 'add' :
      todo = input("Enter a todo")
      todos.append(todo)
    # case 'show' :
    #   for index,item in enumerate(todos):
    #       print(index,'-',item)
    case 'show' :
      for index,item in enumerate(todos):
          row = f"{index}-{item}"
          print(row)
    case 'exit' :
      break

print("Bye")