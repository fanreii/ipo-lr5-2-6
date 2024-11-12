infile = open('text.txt', 'r') # открытие файла текст для чтения
outfile = open('output.txt', 'w') # открытие файла для записи
for line in infile:
    if len(line) > 5:
        outfile.write(line) # запись
