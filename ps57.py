import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout = [[label],[input_box,add_button]],
                   font=("Helventica",20) )
event=window.read()
print(event)
window.close()
