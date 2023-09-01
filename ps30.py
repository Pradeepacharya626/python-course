
                  #DAY 9

# if you want write the user_action input and todo in single line

while True :
  user_action = input("Type add,show,edit,complete or exit") + "\n"
  
  if 'add' in user_action or 'new' in user_action :
    todo = user_action[4:]
    
    with open('ps.txt','r') as file :
      todos = file.readlines()
    
    todos.append(todo)
  
    with open('ps.txt','w') as file :   
      file.writelines(todos)
    
  elif 'show' in user_action :
    file = open('ps.txt','r')
    todos = file.readlines()
    file.close()
    
    for index,item in enumerate(todos):
      item = item.strip('\n')
      row = f"{index+1}-{item}"
      print(row)

  #  if u type edit 2 like this
  elif 'edit' in user_action :
    number = int(user_action[5:])
    number = number-1
    
    with open('ps.txt','r') as file :
      todos = file.readlines()
      
    new_todo = input("Enter new todo")
    todos[number] = new_todo

    with open('ps.txt','w') as file :
      todos = file.writelines(todos)

  #  if u type complete 2 like this
  elif 'complete' in user_action :
    num = int(user_action[9:])

    with open('ps.txt','r') as file :
      todos = file.readlines()

    index = num-1
    todo_to_remove = todos[index].strip('\n') 

    todos.pop(index)
    
    with open('ps.txt','w') as file :
      todos = file.writelines(todos)

    msg = f"todo {todo_to_remove} is removed"
    print(msg)
    
  elif 'exit' in user_action :
    break

  else :
    print("Command is not found")

print("Bye")

