import time
import os
import feedparser
from datetime import datetime

i = 0
newFileName = []
stringSyndi = 'https://www.royalroad.com/syndication/'

for filename in os.listdir(os.getcwd()):
   if filename.startswith("2022-04-29-F"):
      print ("Skip...29")
   elif filename.startswith("2022-04-28-F"):
      print ("Skip...28")
   elif filename.endswith(".py"):
      print ("Py file...")
   else:
      basename = filename
      print (basename)
      rrid_arr = basename.split("-")
      rrid = rrid_arr[3].replace(".md", "")
      rrid_url = rrid.replace("F", stringSyndi)
      NewsFeed = feedparser.parse(rrid_url)
      if NewsFeed.entries:
         entry = NewsFeed.entries[0]
         date_time_str = entry.published.split(" ")
         date_str = date_time_str[1] + " " + date_time_str[2] + " " + date_time_str[3]
         date_time_obj = datetime.strptime(date_str, '%d %b %Y')
         newFileName = date_time_obj.strftime("%Y-%m-%d") + "-" + rrid + ".md"
         delta = datetime.today() - date_time_obj

         if delta.days > 40:
            stringFind = 'ONGOING'
            replaceStatus = 0
            with open(os.path.join(os.getcwd(), filename), 'r+') as rawfile: 
               newContent = ""
               for line in rawfile:
                  if stringFind in line:
                     line = line.replace(stringFind,'HIATUS')
                     replaceStatus = 1
                     print("Line repalced...")
                  newContent = newContent + line
               
               if replaceStatus == 1:
                  rawfile.seek(0)
                  rawfile.write(newContent)
                  break

         i = i + 1
         if i > 30:
            time.sleep(1)
            i = 0
         if newFileName in basename:
            print (".")
         else:
            os.rename(filename, newFileName)

      else:
         print ("Missing"+rrid)
