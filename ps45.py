            #DAY 14

# if def functions are present in another file
#check functions.py for more information

from functions import get_todos,write_todos        #this line is added
    

while True :
  user_action = input("Type add,show,edit,complete or exit") + "\n"
  
  if user_action.startswith("add") :
    todo = user_action[4:]

    todos = get_todos() 
 
    todos.append(todo)
  
    write_todos(todos)
    
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

