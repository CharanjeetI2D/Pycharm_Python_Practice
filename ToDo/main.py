file_path = '/Users/charanjeetsingh/Documents/PythonProjects/Python_ Experiments/ToDo/Todos.txt'


def get_todos(file_name):
    with open(file_name, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(file_path_arg, todos_arg):
    with open(file_path_arg, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input('Type operation: add, show, edit, exit, remove : ').strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        # Reading the file
        todos = get_todos(file_path)

        # adding the new item to todos list
        todos.append(todo + '\n')

        # Create a file object to write to file
        write_todos(file_path, todos)

    elif user_action.startswith('show'):
        # Reading the file
        todos = get_todos(file_path)

        # new_todos = []
        # for items in todos:
        #     new_item = items.strip('\n')
        #     new_todos.append(new_item)

        # List comprehension
        # new_todos = [items.strip('\n') for items in todos]

        for index, items in enumerate(todos):
            item = items.strip('\n')
            all_items = f"{index + 1}-{item}"
            print(all_items)

    elif user_action.startswith('edit'):
        try:
            # Reading the file
            todos = get_todos(file_path)
            print(todos)

            user_input = int(user_action[5:])
            index_position = user_input - 1

            print(f"You have selected '{todos[index_position].strip()}' to change")

            new_todo = input("Enter a new item: ")
            todos[index_position] = new_todo.title() + '\n'
            print("Item edit success")
            print(todos)

            # Writing to File
            write_todos(file_path, todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('remove'):
        try:
            # Take the input form the user
            user_input = int(user_action[len('remove'):])

            # Reading the file
            todos = get_todos(file_path)

            index_position = user_input - 1
            todo_to_remove = todos[index_position].strip()

            todos.pop(index_position)

            # Writing to file
            write_todos(file_path, todos)

            message = f"Todo '{todo_to_remove}' was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("The command is not valid")

print("Bye")
