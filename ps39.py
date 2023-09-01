            #DAY 12

# parameter of the function and argument of the function for ps35.py

def get_todos(filepath) :
  with open(filepath,'r') as file :
    todos = file.readlines()
  return todos


def write_todos(filepath,todos_arg) :
  with open(filepath,'w') as file_local :
    file_local.writelines(todos_arg)     #return is not written in writting mode
    
    

while True :
  user_action = input("Type add,show,edit,complete or exit") + "\n"
  
  if user_action.startswith("add") :
    todo = user_action[4:]

    todos = get_todos("ps.txt")      #todos = get_todos(filepath="ps.txt") 
    
    todos.append(todo)
  
    write_todos("ps.txt",todos)
    
  elif user_action.startswith("show") :

    todos = get_todos("ps.txt")


    for index,item in enumerate(todos):
      item = item.strip('\n')
      row = f"{index+1}-{item}"
      print(row)

  elif user_action.startswith("edit") :
    try :
      number = user_action[5:]                
      number = number-1
      
      todos = get_todos()

      new_todo = input("Enter new todo")
      todos[number] = new_todo
  
      write_todos(todos)

    except TypeError :
      print("invalid command")
      continue
  
  elif user_action.startswith("complete") :
    
    try :                                
      num = user_action[9:]
  
      todos = get_todos("ps.txt")
  
      index = num-1
      todo_to_remove = todos[index].strip('\n') 
  
      todos.pop(index)
      
      write_todos("ps.txt",todos)
  
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

