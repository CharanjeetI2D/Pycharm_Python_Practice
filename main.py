file_path = '/Users/charanjeetsingh/Documents/PythonProjects/Python_ Experiments/Todos.txt'

while True:
    todo_action = input('Type operation: add, show, edit, exit, remove : ').strip()

    if 'add' in todo_action:
        todo = todo_action[4:] + '\n'

        # Reading the file
        with open(file_path, 'r') as file:
            todos = file.readlines()

        # adding the new item to todos list
        todos.append(todo)

        # Create a file object to write to file
        with open(file_path, 'w') as file:
            file.writelines(todos)

    elif 'show' in todo_action:

        with open(file_path, 'r') as read_file:
            todos = read_file.readlines()

        # new_todos = []
        # for items in todos:
        #     new_item = items.strip('\n')
        #     new_todos.append(new_item)

        #List comprehension
       # new_todos = [items.strip('\n') for items in todos]

        for index, items in enumerate(todos):
            item = items.strip('\n')
            all_items = f"{index + 1}-{item}"
            print(all_items)

    elif 'edit' in todo_action:
        with open(file_path, 'r') as read_file:
            todos = read_file.readlines()
        print(todos)

        user_input = int(todo_action[5:])
        index_position = user_input - 1

        print(f"You have selected {todos[index_position]} to change")

        new_todo = input("Enter a new item: ")
        todos[index_position] = new_todo.title() + '\n'
        print("Item edit success")
        print(todos)

        with open(file_path, 'w') as file:
            file.writelines(todos)

    elif 'remove' in todo_action:
        # Take the input form the user
        user_input = int(todo_action[len('remove') + 1:])

        with open(file_path, 'r') as read_file:
            read_file.readlines()

        index_position = user_input - 1
        todo_to_remove = todos[index_position].strip()

        todos.pop(index_position)

        # save the new to dos in a new file
        with open(file_path, 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)

    elif 'exit' in todo_action:
        break

    else:
        print("The command is not valid")

print("Bye")

