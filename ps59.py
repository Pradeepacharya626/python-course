                                                # DAY17


import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo",key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',enable_events=True,size=[45,10])              #enable_events = False (enable_events is optional)
edit_button = sg.Button("edit")

window = sg.Window("My To-Do App",
                   layout = [[label],[input_box,add_button],[list_box,edit_button]],
                   font=("Helventica",15) )


while True :
    event,values=window.read()
    print(event)
    print(values)

    match event :
        case "Add" :
            todos = functions.get_todos()
            new_todo=values["todo"]+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case "edit" :
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos= functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)             #it is used to update the listbox



        case sg.WIN_CLOSED :
            break

window.close()
