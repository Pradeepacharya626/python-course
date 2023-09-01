            #DAY 13

# use of help function to read the docstring

def get_todos(filepath="ps.txt") :    
  ''' get_todos is used to read the to-do items inlist'''
  with open(filepath,'r') as file :
    todos = file.readlines()
  return todos


def write_todos(todos_arg,filepath="ps.txt") :
  with open(filepath,'w') as file_local :
    file_local.writelines(todos_arg)     
    

print(help(get_todos))        #this is used to read the docstring

#press q to overcome end

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
