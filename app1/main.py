from functions import todos_read , todos_write
import time
#from files_ import function

now = time.strftime("%B %d, %Y %H:%M:%S") #
#used to format date and time objects into human-readable
#strings based on a specified format using special format codes
print(f"It is {now}")

while True:
    user_option = input("Enter your choice add,edit,complete,show,exit :")
    user_option = user_option.strip()

    if user_option.startswith('add'):
    # if 'add' not in user_option:
        todo = user_option[4:] + '\n'

        todos = todos_read()

        todos.append(todo.capitalize())

        todos_write(todos)

    elif user_option.startswith('edit'):
        try:
            numbers = int(user_option[5:])
            print(numbers)

            numbers = numbers - 1

            todos = todos_read()

            new_todo = input("Enter new todo: ")
            todos[numbers] = new_todo.capitalize() + '\n'

            todos_write(todos)

        except ValueError:
            print("command not valid")
            continue


    elif user_option.startswith('complete'):
        try:
            number = int(user_option[9:])
            index = number - 1

            todos = todos_read()

            todo_to_complete = todos[index].strip('\n')
            todos.pop(index)

            todos_write(todos)

            message = f"Todo {todo_to_complete} was remove from the list"
            print(message)
        except IndexError:
            print("the list number is out of range")
            continue

    elif user_option.startswith('show'):

        todos = todos_read()

        for index,item in enumerate(todos):
            item=item.strip("\n")
            clean_output = f"{index + 1}-{item}"
            print(clean_output)

    elif user_option.startswith('exit'):
        break

    else:
        print("command not valid")

print("Goodbye")



