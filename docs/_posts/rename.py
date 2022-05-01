import os

newFileName = []
stringFind = 'link: https://www.royalroad.com/fiction/'

for filename in os.listdir(os.getcwd()):
   if filename.startswith("h"):
      with open(os.path.join(os.getcwd(), filename), 'r') as rawfile: 
         for line in rawfile:
            if stringFind in line:
               x = line.split("/")
               newFileName = "2022-03-20-F" + x[4] + ".md"
               break
      os.rename(filename, newFileName)
