import re
import requests
from bs4 import BeautifulSoup
for i in range(2,400,2):
    try:
        url="http://nfs.sparknotes.com/errors/page_"+str(i)+".html"
        r=requests.get(url)
        soup=BeautifulSoup(r.content,'html.parser')
        print soup.prettify()
#         oline=soup.findAll(class_=re.compile("original-line"))
#         op=open('opf.txt','a')
#         oline=str(oline)
#         op.write(oline)
# #         mline=soup.findAll(class_=re.compile("modern-line"))
# #         op.write(str(mline))
# # op.close()
