import PySimpleGUI as sg

label1 = sg.Text("Select the files to compress")
input_box1 = sg.InputText()
choose_but1 = sg.FilesBrowse("choose")

label2 = sg.Text("Select the destination folder")
input_box2 = sg.InputText()
choose_but2 = sg.FolderBrowse("choose")

comp_but = sg.Button("Compress")

window = sg.Window("trial",layout=[[label1,input_box1,choose_but1],[label2,input_box2,choose_but2],[comp_but]])
window.read()
window.close()