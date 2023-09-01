import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo")    #it is not neccessary to write argument..tooltip is used to give hint when mouse is on box

window = sg.Window("My To-Do App",layout = [[label,input_box]] )        #label and input_box in single row
#layout = [[label],[input_box]]  label and input_box in different row
window.read()
window.close()