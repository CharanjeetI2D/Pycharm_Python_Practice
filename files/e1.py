import glob

myfiles = glob.glob("/Users/charanjeetsingh/Documents/PythonProjects/Python_ Experiments/files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())
