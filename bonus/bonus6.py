file1_content = ['Content of file 1',
                 'Contents of file 2',
                 'Contents of file 3']

filenames = ["doc.txt",
             "report.txt",
             "presentation.txt"]

for content, files in zip(file1_content, filenames):
    write_file = open(f"/Users/charanjeetsingh/Documents/PythonProjects/Python_ Experiments/files/{files}", 'w')
    write_file.write(content)

a = "hello" \ 
    "There is " \
    "Nothing"
