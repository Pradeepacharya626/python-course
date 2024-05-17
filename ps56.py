import FreeSimpleGUI as sg


option1 = sg.Radio("birds",group_id="quetion1")
option2 = sg.Radio("mammals",group_id="quetion1")
option3 = sg.Radio("fish",group_id="quetion1")
option4 = sg.Radio("chicken",group_id="quetion1")
option5 = sg.Radio("5",group_id="quetion2")
option6 = sg.Radio("6",group_id="quetion2")

label1 = sg.Text("Amphibians are what")
label2 = sg.Text("pic positive num")

window = sg.Window("Multiple Choice",layout=[[label1],[option1],[option2],[option3],[option4],[label2],[option5,option6]])
window.read()
window.close()
