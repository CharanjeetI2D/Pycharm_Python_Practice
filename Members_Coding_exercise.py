new_member = input("Please enter a new member name: ")

file = open("members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append(new_member + "\n")


file = open("members.txt", 'w')
existing_members = file.writelines(existing_members)
file.close()
