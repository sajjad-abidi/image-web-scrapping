#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import re
import os
from bs4 import BeautifulSoup

user = input("Name of the image to be searched: ")

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

url = f"https://www.google.com/search?q={user}&tbm=isch&sa=X&ved=2ahUKEwiQm6DZofD_AhUS7TgGHcKGC74Q0pQJegQIDRAB&biw=1482&bih=746"

response = requests.get(url=url, headers=user_agent).text

pattern = r"https://[^\"]+\.jpg"

images = re.findall(pattern, response)

print(f"Total {len(images)} Image Found")

no_of_images = int(input("Number of images to be downloaded: "))

if images:
    if not os.path.exists(user):
        os.mkdir(user)
        os.chdir(user)
    else:
        os.chdir(user)

    for image_url in images[:no_of_images]:
        response = requests.get(url=image_url).content
        image_name = image_url.split("/")[-1]

        with open(image_name, "wb") as file:
            file.write(response)


# In[ ]:




