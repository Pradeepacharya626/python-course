                                                # DAY18
# implementation over ps60.py

import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo",key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',enable_events=True,size=[45,15])
edit_button = sg.Button("edit")
complete_button = sg.Button("complete")
exit_button = sg.Button("exit")

window = sg.Window("My To-Do App",
                   layout = [[label],[input_box,add_button],
                             [list_box,edit_button,complete_button],
                             [exit_button]],
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
            window["todos"].update(values=todos)
        case "edit" :
            try :
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']+"\n"
                todos= functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError :
                sg.popup("Please select the item first",font=("Helvetica",20))

        case "complete" :
            try :
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value='')
            except IndexError :
                sg.popup("Please select the item first", font=("Helvetica", 20))
        case "exit" :
            break
        case "todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED :
            break

window.close()
