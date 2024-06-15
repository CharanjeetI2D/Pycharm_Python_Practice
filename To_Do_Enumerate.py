todos = ['Cleaning', 'washing', 'programming']

while True:
    todo_action = input('Type operation: add, show, edit, exit, complete : ').strip()

    match todo_action:

        case 'add':
            new_item = input("Please enter value to add: ")
            todos.append(new_item)

        case 'display' | 'show':
            for items in todos:
                all_items = f"{todos.index(items) + 1} {items}"
                print(all_items)

        case 'edit':
            print("Below are all the items")
            for item_index, items in enumerate(todos):
                row = f"{item_index + 1}-{items}"
                print(row)
            item_index = int(input("Which item number would want to edit from above?: "))
            print(f"You have selected {todos[item_index - 1]} to change")
            new_item = input("Enter a new item: ")
            todos[item_index - 1] = new_item
            print("Item edit success")
            print(todos)

        case 'complete' | 'remove':
            for item_index, item in enumerate(todos):
                item_string = f"{item_index + 1} : {item}"
                print(item_string)
            user_input = int(input("Please enter item number you want to remove: "))
            todos.pop(user_input - 1)
            print(f"New list: ", todos)




        case 'exit' | 'quit':
            break

