# import libraries
import requests as req 
import time  # incase of falling request 
from bs4 import BeautifulSoup
import os
# fake headers عشان اضحك علي الموقع

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/154.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}

# first get the html page
for i in range(3):
 try:
   
   res = req.get(url="https://en.wikipedia.org/wiki/Cristiano_Ronaldo" , timeout=4 , headers=headers)
   res.raise_for_status()
   html_page = res.text
   print("=> the request succeded")
   break
 
 except Exception as error :
   print(f"the request has faild tries : {i}")
   time.sleep(3)

# second parse that page using bs4

soup = BeautifulSoup(html_page , "html.parser")

for st in soup.find_all("p"):
  
  if not os.path.exists("Data"):
   os.mkdir("/Data")

  with open("Data/ronaldo_wiki.txt","a") as f:
      if not st.get_text().isspace():
         f.write(f"{st.get_text()}\n")
         
