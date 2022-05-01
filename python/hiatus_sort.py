import os

newFileName = []
statusFind = 'HIATUS'

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".md"):
        with open(os.path.join(os.getcwd(), filename), 'r') as rawfile: 
            for line in rawfile:
                if statusFind in line:
                    newFileName = "h" + filename
                    os.rename(filename, str(newFileName))
                    break
            
