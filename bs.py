import requests
from bs4 import BeautifulSoup
import os

parent_dir = 'D:\\Skeleton Warrior'

def get_image_list(link):
        url = link.a['href']
        r = requests.get(url=url,headers=headers)

        soup = BeautifulSoup(r.content, features="html.parser")

        section = soup.find('div', attrs={'class':'entry-content'})


        images = section.findAll('div', attrs={'class':'separator'})

        i=1

        split_url = images[0].img['src'].split('/')
        ext = split_url[-1]
        ext = ext.split('.')[1]
        print(ext)
        for part in split_url:
                if 'chapter' in part.lower():
                    directory = part.title()
                    path = os.path.join(parent_dir,directory)
                    os.mkdir(path)
                    os.chdir(path)
                    break
                    
        for image in images:
            filename = f'{i}.{ext}' 
            img = image.img['src']
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
   








