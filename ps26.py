            #DAY 8

# Another methode to open file
# making changes in 'edit' case
# making changes in 'complete' case

while True :
  user = input("Type add,show,edit,complete or exit")
  user = user.strip()     
  match user :
    case 'add' :
      todo = input("Enter a todo") + "\n"
      
      with open('ps.txt','r') as file :
        todos = file.readlines()
      
      todos.append(todo)
    
      with open('ps.txt','w') as file :   # There is no need to close the file (file.close())
        file.writelines(todos)
      
    case 'show' :
      file = open('ps.txt','r')
      todos = file.readlines()
      file.close()
      
      for index,item in enumerate(todos):
        item = item.strip('\n')
        row = f"{index+1}-{item}"
        print(row)
    case 'edit' :
      number = int(input("Enter the number of todo to edit"))
      number = number-1
      
      with open('ps.txt','r') as file :
        todos = file.readlines()
        
      new_todo = input("Enter new todo")
      todos[number] = new_todo

      with open('ps.txt','w') as file :
        todos = file.writelines(todos)
      
    case 'complete' :
      num = int(input("Enter the todo number"))

      with open('ps.txt','r') as file :
        todos = file.readlines()

      index = num-1
      todo_to_remove = todos[index].strip('\n') 

      todos.pop(index)
      
      with open('ps.txt','w') as file :
        todos = file.writelines(todos)

      msg = f"todo {todo_to_remove} is removed"
      print(msg)
      
    case 'exit' :
      break

print("Bye")

