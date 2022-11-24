import os

i = 0
newFileName = []



for filename in os.listdir(os.getcwd()):
   if filename.startswith("2022-11-24-F"):
      print ("New File!")
      with open(os.path.join(os.getcwd(), filename), 'r+') as checkFile: 
        for line in checkFile:
