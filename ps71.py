                                                #DAY 18
#implimentation over ps69.py
#sometimes widgets are not well assigned ,that avoided by using columns

import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("Black")

label1 = sg.Text("select the archive : ")
input1 = sg.InputText()
choose_button1 = sg.FileBrowse("choose",key="archive")

label2 = sg.Text("select the destination directory : ")
input2 = sg.InputText()
choose_button2 = sg.FolderBrowse("choose",key="folder")

extract_button = sg.Button("Extract")
out_box = sg.Text(key="output",text_color="Green")

#use columns
column1=sg.Column([[label1],[label2]])
column2=sg.Column([[input1],[input2]])
column3=sg.Column([[choose_button1],[choose_button2]])


window = sg.Window("Archive Extractor",
                   layout=[[column1,column2,column3],
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