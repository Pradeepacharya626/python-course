            #DAY 7

# To overcome the problem in show case(i.s it shows 2 lines gap)

while True :
  user = input("Type add,show,complete or exit")
  user = user.strip()     
  match user :
    case 'add' :
      todo = input("Enter a todo") + "\n"
      file = open('ps.txt','r')
      todos = file.readlines()
      file.close()
      todos.append(todo)
      file = open('ps.txt','w')
      file.writelines(todos)
      file.close()
    case 'show' :
      file = open('ps.txt','r')
      todos = file.readlines()
      file.close()
      new_todos = []
      for item in todos :
        new_item = item.strip('\n')
        new_todos.append(new_item)
      for index,item in enumerate(new_todos):
          row = f"{index+1}-{item}"
          print(row)
    case 'edit' :
      file = open('ps.txt', 'r')
      todos = file.readlines()
      number = int(input("Enter the todo to edit"))
      number = number-1
      new_todo = input("Enter new todo")
      todos[number] = new_todo
    case 'complete' :
      num = int(input("Enter the todo number"))
      todos.pop(num-1)
    case 'exit' :
      break

print("Bye")

