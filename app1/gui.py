import functions
import FreeSimpleGUI as app
text_box = app.Text("Type in a to-do")
input_box = app.InputText(tooltip="Enter to-do",key= "todo")
add_button = app.Button("Add")

list_box = app.Listbox(values=functions.todos_read(),key='list',
                        enable_events=True,size=[45, 10])
edit_button = app.Button("Edit")


window = app.Window("To-Do App",
                    layout=[[text_box],[input_box, add_button],
                    [list_box,edit_button]],
                    font = ("helvetica", 20 ))
while True:
    event ,value = window.read()
    print(event)
    print(value)
    print(value["list"])
    match event:
        case 'Add':
           todos = functions.todos_read()
           new_todos = value["todo"] + '\n'
           todos.append(new_todos.capitalize())
           functions.todos_write(todos)
           window["list"].update(values=todos)

        case 'Edit':
            todo_to_edit = value["list"][0]
            new_todo = value["todo"] + '\n'

            todos= functions.todos_read()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo.capitalize()
            functions.todos_write(todos)
            window["list"].update(values=todos)

        case 'list':
            window['todo'].update(value=value['list'][0])


        case app.WIN_CLOSED:
            break



window.close()