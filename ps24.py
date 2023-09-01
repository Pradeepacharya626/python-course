            #DAY 7

# use of different method for ps22.py and ps23.py to remove \n

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
      
      for index,item in enumerate(todos):
        item = item.strip('\n')
        row = f"{index+1}-{item}"
        print(row)
    case 'complete' :
      num = int(input("Enter the todo number"))
      todos.pop(num-1)
    case 'exit' :
      break

print("Bye")

