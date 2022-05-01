import requests
import re
import os

newFileName = []
stat_complete = 0
stringFind = 'link: https://www.royalroad.com/fiction/'

for filename in os.listdir(os.getcwd()):
   if filename.startswith("h"):
      with open(os.path.join(os.getcwd(), filename), 'r+') as rawfile: 
         newContent = ""
         for line in rawfile:
            if stringFind in line:
               x = line.split("/")

               url = "https://www.royalroad.com/fiction/" + x[4]
               print (url)
               r = requests.get(url)
               r.text
               matches = re.findall('COMPLETED', r.text)

               if len(matches) == 0: 
                  print ('.')

               else:
                  newFileName = filename.replace('h','')
                  stat_complete = 1

         for line in rawfile:
            if 'HIATUS' in line:
               if stat_complete == 1:
                  line = line.replace('HIATUS','COMPLETED')
            newContent = newContent + line
         
         if stat_complete == 1:
            rawfile.seek(0)
            rawfile.write(newContent)
            os.rename(filename, newFileName)
            stat_complete = 0
            print ("Change status...")




