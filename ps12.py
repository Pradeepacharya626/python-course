              #DAY 5

      #TO GET THE LIST FROM 1 AND REMOVE(COMPLETE)

todos = []

while True :
  user = input("Type add,show,complete or exit")
  user = user.strip()      # used to convert "add " to "add"
  match user :
    case 'add' :
      todo = input("Enter a todo")
      todos.append(todo)
    # case 'show' :
    #   for index,item in enumerate(todos):
    #       print(index,'-',item)
    case 'show' :
      for index,item in enumerate(todos):
          row = f"{index+1}-{item}"
          print(row)
      print(index,item)#after coming out from the for loop also it is still working
      print(f"hello{index+1}-{item}")
    case 'complete' :
      num = int(input("Enter the todo number"))
      todos.pop(num-1)
    case 'exit' :
      break

print("Bye")


for i,j in enumerate("Hello") :
  print(i,j)

a = enumerate("Hello")
print(list(a))