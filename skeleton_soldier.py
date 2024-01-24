"""_summary_
This script scrapes a website for all 
Skeleton Soldier Comics 
and saves them in a folder.
Make sure you havve BeautifulSoup installed:

      pip install beautifulsoup4

You must create the initial directory 
where you want the comics stored and 
make sure the parent_dir matches the
location of the folder.

Run the script and enjoy the comics.
"""
import requests
from bs4 import BeautifulSoup
import os

parent_dir = 'D:\\Skeleton Warrior'  #This is the folder you created.  

def get_image_list(link):
      url = link.a['href']
      r = requests.get(url=url,headers=headers)

      soup = BeautifulSoup(r.content, features="html.parser")

      section = soup.find('div', attrs={'class':'entry-content'})


      images = section.findAll('img', attrs={'decoding':'async'})

      i=1
      split_url = images[0]['src'].split('/')
      ext = split_url[-1]
      ext = ext.split('.')[1]
      for part in split_url:
            if 'chapter' in part.lower():
                  try:
                        directory = part.title()
                        path = os.path.join(parent_dir,directory)
                        os.mkdir(path)
                        os.chdir(path)
                        break
                  except:
                        pass
   
      for image in images:
            filename = f'{i}.{ext}' 
            img = image['src']
            print (img)
            flag = requests.get(img, headers=headers)
            if flag.status_code != 200:
                  print('Error getting ')
            with open(filename, 'wb') as f:
                  noop = f.write(flag.content)
            i += 1             

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
url = "https://skeleton-soldier.online/"
r = requests.get(url=url,headers=headers)

soup = BeautifulSoup(r.content, features="html.parser")
section = soup.find('ul',attrs={'class':'su-posts su-posts-list-loop'})
links = section.findAll('li')
i = len(links)
for link in links:
     get_image_list(link)