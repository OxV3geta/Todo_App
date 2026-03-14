import functions
import FreeSimpleGUI as app
text_box = app.Text("Type in a to-do")
input_box = app.InputText(tooltip="Enter to-do",key= "todo")
add_button = app.Button("Add")
window = app.Window("To-Do App",
                    layout=[[text_box],[input_box, add_button]] ,
                    font = ("helvetica", 20 ))
while True:
    event ,value = window.read()
    print(event)
    print(value)
    match event:
        case 'Add':
           todos = functions.todos_read()
           new_todos = value["todo"] + '\n'
           todos.append(new_todos)
           functions.todos_write(todos)
        case app.WIN_CLOSED:
            break





window.close()