todos = ['tomato', 'potato', 'sulami']

while True:
    todo_action = input('Type operation: add, show, edit, exit : ').strip()

    match todo_action:

        case 'add':
            new_item = input("Please enter value to add: ")
            todos.append(new_item)

        case 'display' | 'show':
            for items in todos:
                print(items)

        case 'edit':
            print("Below are all the items")
            for items in todos:
                print((todos.index(items) + 1), " ", items)
            item_index = int(input("Which item number would want to edit from above?: "))
            item_index = item_index - 1
            new_item = input("Enter a new item: ")
            todos[item_index] = new_item
            print("Item edit success")
            print(todos)
        case 'exit' | 'quit':
            break

