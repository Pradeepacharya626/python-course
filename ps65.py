                                                #DAY 17

#write the contents in different column
import PySimpleGUI as sg

left_content = [[sg.Text("left1")],[sg.Text("left2")],[sg.Text("left3")]]
right_content = [[sg.Text("right1")],[sg.Text("right2")],[sg.Text("right3")]]

left_column = sg.Column(left_content)
right_column = sg.Column(right_content)

layout = [[left_column,right_column]]

window = sg.Window("column",layout=layout)
window.read()
window.close()