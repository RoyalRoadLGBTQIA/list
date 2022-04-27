import os

stringFind = 'link: https://www.royalroad.com/fiction/'

for filename in os.listdir(os.getcwd()):
   if filename.endswith(".md"):
      with open(os.path.join(os.getcwd(), filename), 'r') as rawfile: 
         for line in rawfile:
            if stringFind in line:
               file_object = open('RRID.txt', 'a')
               file_object.write(line)
               file_object.close()
               break