              #DAY 6

# if the text file is present in another folder or directry

while True :
  user = input("Type add,show,complete or exit")
  user = user.strip()     
  match user :
    case 'add' :
      todo = input("Enter a todo") + "\n"
      file = open('pradeep/pradi/ps1.txt','r')
      todos = file.readlines()
      file.close()
      todos.append(todo)
      file = open('pradeep/pradi/ps1.txt','w')
      file.writelines(todos)
      file.close()
    case 'show' :
      file = open('pradeep/pradi/ps1.txt','r')
      todos = file.readlines()
      file.close()
      for index,item in enumerate(todos):
          row = f"{index+1}-{item}"
          print(row)
    case 'complete' :
      num = int(input("Enter the todo number"))
      todos.pop(num-1)
    case 'exit' :
      break

print("Bye")


