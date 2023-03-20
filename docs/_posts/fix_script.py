import time
import os
import io
import feedparser, requests, time
from datetime import datetime

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

i = 0
newFileName = []
stringSyndi = 'https://www.royalroad.com/fiction/syndication/'

for filename in os.listdir(os.getcwd()):
   if filename.startswith("2023-03-20"):
      print ("Skip...3")
   elif filename.startswith("2021"):
      print ("Skip...2021 done")
   elif filename.startswith("2020"):
      print ("Skip...2020 done")
   elif filename.startswith("2019"):
      print ("Skip...2019 done")
   elif filename.startswith("2018"):
      print ("Skip...2018 done")
   elif filename.startswith("2017"):
      print ("Skip...2017 done")
   elif filename.startswith("2016"):
      print ("Skip...2016 done")
   elif filename.startswith("h2"):
      print ("Skip...hiatus...")
   elif filename.endswith(".py"):
      print ("Py file...")
   elif filename.startswith("2023-"):
      preStrFind = 'ONGOING'
      strOngoing = False
      with open(os.path.join(os.getcwd(), filename), 'r+') as checkFile: 
         for line in checkFile:
            if preStrFind in line:
               strOngoing = True
               break
      
      if strOngoing is True:
         print("Check Ongoing stories...")
         basename = filename
         print (basename)
         rrid_arr = basename.split("-")
         rrid = rrid_arr[3].replace(".md", "")
         if rrid.__contains__("F") is True:
            rrid_url = rrid.replace("F", stringSyndi)
         else:
            rrid_url = rrid.replace("Z", stringSyndi)
         
         print (rrid_url)

         response = requests.get(rrid_url, headers=headers, timeout=100)
         #print (response.content)
         content = io.BytesIO(response.content.strip())

         NewsFeed = feedparser.parse(content)
         print ("---")
         if NewsFeed.entries:
            entry = NewsFeed.entries[0]
            date_time_str = entry.published.split(" ")
            date_str = date_time_str[1] + " " + date_time_str[2] + " " + date_time_str[3]
            date_time_obj = datetime.strptime(date_str, '%d %b %Y')
            newFileName = date_time_obj.strftime("%Y-%m-%d") + "-" + rrid + ".md"
            delta = datetime.today() - date_time_obj

            if delta.days > 60:
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
            if newFileName not in basename:
               os.rename(filename, newFileName)

         else:
            print ("Missing "+rrid)
