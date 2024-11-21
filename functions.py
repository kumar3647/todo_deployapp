def get_todos(filepath="files/todos.txt"):
    """ Get todos from the file path as default path is files/todos.txt """
    with open(filepath, "r") as file_local:
        todolist_local = file_local.readlines()
    return todolist_local

def write_todos(todolist_local, filepath="files/todos.txt"):
    """ write todos to the filepath as default path is files/todos.txt """
    with open(filepath, "w") as file_local:
        file_local.writelines(todolist_local)


if __name__ == "__main__":
    print("I'm in functions")