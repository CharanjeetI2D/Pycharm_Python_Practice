filenames = ["1.doc", "1.report", "1.presentation"]
print(filenames)
filenames = [file_item.replace(".", "-") + '.txt' for file_item in filenames]
print(filenames)