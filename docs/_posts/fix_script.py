import time
import os
import feedparser
from datetime import datetime

i = 0
newFileName = []
stringSyndi = 'https://www.royalroad.com/syndication/'

for filename in os.listdir(os.getcwd()):
   if filename.endswith(".md"):
      basename = os.path.basename(filename)
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
         i = i + 1
         if i > 30:
            time.sleep(1)
            i = 0

         if newFileName in basename:
            print ("match: " + i)
         else:
            os.rename(filename, newFileName)

      else:
         print ("Missing"+rrid)
