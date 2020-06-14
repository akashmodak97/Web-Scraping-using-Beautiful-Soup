# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 04:45:51 2019

@author: Akash
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup


urlname = "https://www.anandabazar.com/sport/the-pink-ball-test-liton-das-and-naeem-hasan-ruled-out-from-eden-test-dgtl-1.1074029"
try:
    page = urlopen(urlname)
except:
    print("Error in loading page...");
    
soup = BeautifulSoup(page,'html.parser')
content = soup.find('div',{'class':'articleBody'})

article = ''
for i in content.findAll('p'):
    article = article + ' ' + i.text
print(article)

file = open("E:\\snltr corpus\\16.txt","w+",encoding="utf-8")
file.write(article)
