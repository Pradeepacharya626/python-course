            #DAY 11

# if u have a function line many times can use function call
#def .........() :

def get_todos() :
  with open('ps.txt','r') as file :
    todos = file.readlines()
  return todos
    

while True :
  user_action = input("Type add,show,edit,complete or exit") + "\n"
  
  if user_action.startswith("add") :
    todo = user_action[4:]

    todos = get_todos()
    
    todos.append(todo)
  
    with open('ps.txt','w') as file :   
      file.writelines(todos)
    
  elif user_action.startswith("show") :

    todos = get_todos()


    for index,item in enumerate(todos):
      item = item.strip('\n')
      row = f"{index+1}-{item}"
      print(row)

  elif user_action.startswith("edit") :
    try :
      number = int(user_action[5:])                
      number = number-1
      
      todos = get_todos()

      new_todo = input("Enter new todo") + "\n"
      todos[number] = new_todo
  
      with open('ps.txt','w') as file :
        todos = file.writelines(todos)

    except TypeError :
      print("invalid command")
      continue
  
  elif user_action.startswith("complete") :
    
    try :                                
      num = int(user_action[9:])
  
      todos = get_todos()
  
      index = num-1
      todo_to_remove = todos[index].strip('\n') 
  
      todos.pop(index)
      
      with open('ps.txt','w') as file :
        todos = file.writelines(todos)
  
      msg = f"todo {todo_to_remove} is removed"
      print(msg)

    except IndexError :            
      print("invalid command")
      continue
      
      
  elif user_action.startswith("exit") :
    break

  else :
    print("Command is not found")

print("Bye")

