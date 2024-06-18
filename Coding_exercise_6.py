filenames = ['doc.txt', 'report.txt', 'presenation.txt']

for f_name in filenames:
    write_file = open(f_name, 'w')
    write_file.write('hello')
    write_file.close()

