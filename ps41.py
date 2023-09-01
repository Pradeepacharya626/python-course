            #DAY 13

# some of changes to ps35.py

def get_todos(filepath="ps.txt") :        #here "ps.txt" is default value
  with open(filepath,'r') as file :
    todos = file.readlines()
  return todos


def write_todos(todos_arg,filepath="ps.txt") : #non-default arguement is written before default arguement
  with open(filepath,'w') as file_local :
    file_local.writelines(todos_arg)     
    
    

while True :
  user_action = input("Type add,show,edit,complete or exit") + "\n"
  
  if user_action.startswith("add") :
    todo = user_action[4:]

    todos = get_todos() 
    #todos = get_todos("file.txt")         #here "file.txt" is non-defalt value

    
    todos.append(todo)
  
    write_todos(todos)
    # write_todos(todos,"ps.txt")
    # write_todos(filepath="ps.txt",todos_arg=todos)
    
  elif user_action.startswith("show") :

    todos = get_todos("ps.txt")


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
  
      write_todos(todos)

    except TypeError :
      print("invalid command")
      continue
  
  elif user_action.startswith("complete") :
    
    try :                                
      num = int(user_action[9:])
  
      todos = get_todos("ps.txt")
  
      index = num-1
      todo_to_remove = todos[index].strip('\n') 
  
      todos.pop(index)
      
      write_todos(todos)
  
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

