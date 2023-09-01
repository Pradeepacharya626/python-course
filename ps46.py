            #DAY 14

# another method for def functions which  are present in another file

import functions      #here
#from pradeep import functions     #if functions.py is present in another directry

while True :
  user_action = input("Type add,show,edit,complete or exit") + "\n"
  
  if user_action.startswith("add") :
    todo = user_action[4:]

    todos = functions.get_todos()     #changed in many lines like this
 
    todos.append(todo)
  
    functions.write_todos(todos)
    
  elif user_action.startswith("show") :

    todos = functions.get_todos("ps.txt")


    for index,item in enumerate(todos):
      item = item.strip('\n')
      row = f"{index+1}-{item}"
      print(row)

  elif user_action.startswith("edit") :
    try :
      number = int(user_action[5:])                
      number = number-1
      
      todos = functions.get_todos()

      new_todo = input("Enter new todo") + "\n"
      todos[number] = new_todo
  
      functions.write_todos(todos)

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

