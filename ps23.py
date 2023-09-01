            #DAY 7

# use of different method for ps22.py

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

      new_todos = [item.strip('\n') for item in todos]
      
      for index,item in enumerate(new_todos):
          row = f"{index+1}-{item}"
          print(row)
    case 'complete' :
      num = int(input("Enter the todo number"))
      todos.pop(num-1)
    case 'exit' :
      break

print("Bye")

