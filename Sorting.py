waiting_list = ['sen', 'Ben', 'John']
waiting_list.sort(reverse=True)

for index, items in enumerate(waiting_list):
    print(f"{index + 1}.{items.capitalize()}")