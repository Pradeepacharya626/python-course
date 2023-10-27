                                                #DAY 18

import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("Black")

label1 = sg.Text("select the archive : ")
input1 = sg.InputText()
choose_button1 = sg.FileBrowse("choose",key="archive")

label2 = sg.Text("select the dest dir : ")
input2 = sg.InputText()
choose_button2 = sg.FolderBrowse("choose",key="folder")

extract_button = sg.Button("Extract")
out_box = sg.Text(key="output",text_color="Green")

window = sg.Window("Archive Extractor",
                   layout=[[label1,input1,choose_button1],
                           [label2,input2,choose_button2],
                           [extract_button,out_box]])
while True :
    event,values = window.read()
    print(event,values)
    match event :
        case "Extract" :
            archivepath = values["archive"]
            folderpath = values["folder"]
            extract_archive(archivepath,folderpath)
            window["output"].update(value="Extraction successful")

        case sg.WIN_CLOSED :
            break

window.close()