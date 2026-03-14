FILEPATH = "todos.txt" #This is a Constant not variable! so the value is very important

def todos_read(filepath=FILEPATH):
    """Read the text file and return the list of todos"""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

# print(help(todos_read))

def todos_write(todos_arg ,filepath=FILEPATH):
    """" Write the text file and return the list of todos"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)



# print(__name__)
if __name__ == "__main__":
    print("hello")