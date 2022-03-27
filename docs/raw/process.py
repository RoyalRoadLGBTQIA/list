i = 0
filenames = []
with open('filename9.txt') as namefile:
    filenames = namefile.readlines()

infolines = []
with open ("raw_part9.txt", "r") as rawfile:
    for line in rawfile:
        if "==MDEND==" in line:
            a_string = "".join(infolines)
            file = open(filenames[i].strip('\n'), 'w')
            file.write(a_string)
            file.close()
            i = i + 1
            infolines = []
            a_string = ""
        else:
            infolines.append(line)
