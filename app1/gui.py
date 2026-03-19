import functions
import FreeSimpleGUI as app
import time

app.theme("NeonYellow1")
clock = app.Text("" , key="clock")
text_box = app.Text("Type To-Do")
input_box =app.InputText(tooltip="Enter todo",key="input_box")
add_button = app.Button("Add")

list_box = app.Listbox(values= functions.todos_read(),key ='list',
                       enable_events= True ,size=[45,10])
edit_button = app.Button("Edit")

complete_button = app.Button("Complete")
exit_Button = app.Button("Exit")


window = app.Window("To-Do APP",
                    layout = [[clock],
                    [text_box],[input_box,add_button,edit_button],
                    [list_box,complete_button,exit_Button]],
                    font = ("helvetica" , 15))

while True:
    event,value = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%B %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos =functions.todos_read()
            new_todos = value["input_box"] + '\n'
            todos.append(new_todos.capitalize())
            functions.todos_write(todos)
            window["list"].update(values=todos)

        case "Edit":
            try:
                todos = functions.todos_read()
                todo_to_edit = value["list"][0]
                new_todos = value["input_box"] + '\n'
                index = todos.index(todo_to_edit)
                todos[index] = new_todos.capitalize()
                functions.todos_write(todos)
                window["list"].update(values=todos)
            except IndexError:
                app.popup("please select a item first",font= ("helvetica" , 20))

        case "Complete":
            try:
                todos = functions.todos_read()
                todos_to_complete = value["list"][0]
                todos.remove(todos_to_complete)
                functions.todos_write(todos)
                window["list"].update(values=todos)
                window['input_box'].update(value='')
            except IndexError:
                app.popup("please select a item first", font=("helvetica", 20))

        case "Exit":
            break

        case 'list':
            window["input_box"].update(value=value["list"][0])
        case app.WIN_CLOSED:
            break

window.close()


