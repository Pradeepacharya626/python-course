            #DAY 10

'''if u write "show add a new" ,it will go to add.
     to overcome this use below function ''' 


while True :
  user_action = input("Type add,show,edit,complete or exit") + "\n"
  
  if user_action.startswith("add") :
    todo = user_action[4:]
    
    with open('ps.txt','r') as file :
      todos = file.readlines()
    
    todos.append(todo)
  
    with open('ps.txt','w') as file :   
      file.writelines(todos)
    
  elif user_action.startswith("show") :
    file = open('ps.txt','r')
    todos = file.readlines()
    file.close()
    
    for index,item in enumerate(todos):
      item = item.strip('\n')
      row = f"{index+1}-{item}"
      print(row)

  elif user_action.startswith("edit") :
    number = user_action[5:]
    number = number-1
    
    with open('ps.txt','r') as file :
      todos = file.readlines()
      
    new_todo = input("Enter new todo")
    todos[number] = new_todo

    with open('ps.txt','w') as file :
      todos = file.writelines(todos)

  elif user_action.startswith("complete") :
    num = user_action[9:]

    with open('ps.txt','r') as file :
      todos = file.readlines()

    index = num-1
    todo_to_remove = todos[index].strip('\n') 

    todos.pop(index)
    
    with open('ps.txt','w') as file :
      todos = file.writelines(todos)

    msg = f"todo {todo_to_remove} is removed"
    print(msg)
    
  elif user_action.startswith("exit") :
    break

  else :
    print("Command is not found")

print("Bye")

