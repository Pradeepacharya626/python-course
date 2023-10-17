                                            #DAY 17
                           # implimentation over ps62.py ----color change

import PySimpleGUI as sg
from zip_creater import make_archive

label1 = sg.Text("Select the files to compress",text_color="yellow")
input_box1 = sg.InputText()
choose_but1 = sg.FilesBrowse("choose",key="files",button_color="orange")

label2 = sg.Text("Select the destination folder",text_color="yellow")
input_box2 = sg.InputText()
choose_but2 = sg.FolderBrowse("choose",key="folder",button_color="orange")

comp_but = sg.Button("Compress")
output_label = sg.Text(key="output",text_color="red")

window = sg.Window("trial",layout=[[label1,input_box1,choose_but1],[label2,input_box2,choose_but2],[comp_but,output_label]],background_color="skyblue")


while True :
    event,values = window.read()
    print(event,values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths,folder)
    window["output"].update(value="compression successful")



window.close()