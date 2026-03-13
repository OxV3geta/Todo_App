import functions
import FreeSimpleGUI as app
text_box = app.Text("Type in a to-do")
input_box = app.InputText(tooltip="Enter to-do")
add_button = app.Button("Add")
window = app.Window("To-Do App", layout=[[text_box],[input_box, add_button]])
window.read()
window.close()