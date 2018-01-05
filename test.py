import re
import requests
from bs4 import BeautifulSoup
temp4=soup2.find_all(href=re.compile("page"))
for a in temp4:
        a=str(a)
        a=a.split('_')
        a=a[1]
        a=a.split('.')
        a=a[0]
        al.append(int(a))

for i in range(al[0],al[-1],2):
        url="http://nfs.sparknotes.com/errors/page_"+str(i)+".html"
        r=requests.get(url)
        soup=BeautifulSoup(r.content,'html.parser')
        oline=soup.findAll(class_=re.compile("original-line"))
        
        op=open('opf2.txt','a')
        oline=str(oline)
        op.write(oline)
        op.close()
