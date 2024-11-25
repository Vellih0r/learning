new_file = open("sorted.txt", 'w', encoding='utf8')
with open("english.txt", "r", encoding='utf8') as file:
    lines = file.readlines()
    lines = sorted(lines)

    previous = ''
    for line in lines:
        current = line[0]
        if current == '\n':
            continue
        if previous != current:
            new_file.write('-'*37 + '\n\n')
        new_file.write(line)
        previous = line[0]
new_file.close()

    # types of work fith a file
#open('file', 'r') # read only
#open('file', 'w') # create & write OR rewrite file
#open('file', 'a') # (append) create or append in the end
#open('file', 'b') # binary (rb/wb/ab)
#open('file', 'r+') # read + write (if no file -> FileNotFoundError)
#open('file', 'w+') # read + write/rewrite
#open('file', 'a+') # read + append in the end of a file