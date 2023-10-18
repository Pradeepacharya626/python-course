                                            #DAY 17
                                       #Convert to meter

import PySimpleGUI as sg

label_1 = sg.Text("Enter feet")
feet_box = sg.InputText(key="feet")

label_2 = sg.Text("Enter inches")
inch_box = sg.InputText(key="inch")

convert_button = sg.Button("convert")
output_text = sg.Text(key="output")

window = sg.Window("",layout=[[label_1,feet_box],[label_2,inch_box],[convert_button,output_text]])

while True :
    event,values = window.read()
    print(event,values)
    value_metre = float(values["feet"])*0.305+float(values["inch"])*0.0254
    window["output"].update(value=value_metre)

window.close()