import requests
import re

url = 'https://www.royalroad.com/fiction/52068/claras-handbook-of-cliched-romance'
r = requests.get(url)
r.text

matches = re.findall('HIATUS', r.text)

if len(matches) == 0: 
   print ('I did not find anything')
else:
   print ('My string is in the html')