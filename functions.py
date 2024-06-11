def get_todo(filepath='todos.txt'):
    with open(filepath, 'r') as file_read:
        todos_2 = file_read.readlines()
        return todos_2


def write_todo(todo_arg, filepath='todos.txt'):
    with open(filepath, 'w') as file_write:
        file_write.writelines(todo_arg)


