with open('text.txt', 'r') as text:
    with open('temp.txt', 'w') as new_txt:
        for line in text.readlines():
            new_txt.write(line[15:20] + '\n')
