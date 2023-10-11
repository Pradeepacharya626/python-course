import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo",key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout = [[label],[input_box,add_button]],
                   font=("Helventica",20) )



while True :
    event,values=window.read()
    print(event)
    print(values)
    todos = functions.get_todos()
    new_todo=values["todo"]+"\n"
    todos.append(new_todo)
    functions.write_todos(todos)


window.close()
