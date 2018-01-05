import re
import requests
from bs4 import BeautifulSoup
url="http://nfs.sparknotes.com/"
bucket_names=[]
bucket_url=[]
new_bucket=[]
new_names=[]
r=requests.get(url)
print("_______")*21
soup=BeautifulSoup(r.content,'html.parser')
my_tags=soup.find_all(class_=re.compile("entry"))
#print my_tags
for tag in my_tags:
         try:
             temp=str(tag)
             k=temp.split('<a href="')
             temp=k[1]
             w=temp.split('">')
             bucket_url.append(url+str(w[0]))



         except:
             pass

for name in my_tags:
         try:
             temp2=str(name)
             k2=temp2.split('/">')
             temp2=k2[1]
             w2=temp2.split('</a>')
             bucket_names.append(w2[0])

         except:
             pass
# print bucket_names
# for i in range(len(bucket_names)-1):
#     print bucket_names[i]
#Now moving on to page 2
#Testing with a page if sucess lets plan a loop
i=0
for i in range(len(bucket_names)):
     print str(i+1)+")"+" "+bucket_names[i]
#print bucket_url
#-------------------------Page 2 ----------------------------------------------
choice=input("Enter the number of Play of your choice  ")
filename=bucket_names[choice-1]
new_url=bucket_url[choice-1]
new_req=requests.get(str(new_url))
soup2=BeautifulSoup(new_req.content,'html.parser')
temp4=soup2.find_all(href=re.compile("page"))

# Should modify the act and scene urls and able to grab them

for tagss in temp4:
    temp6=str(tagss)
    temp6=temp6.split('">')
    temp6=temp6[1]
    temp6=temp6.split('</a>')
    new_names.append(temp6[0])
    temp5=str(tagss)
    temp5=temp5.split('<a href="')
    temp5=temp5[1]
    temp5=temp5.split('">')
    new_bucket.append(temp5[0])
for x in range(len(new_names)):
    print str(x+1)+")"+" "+new_names[x]

choice_2=input("Enter the number of Act of your choice ")
#-------------------------------Page 3 ----------------------------------
actname=new_names[choice_2-1]
req3=requests.get(new_bucket[choice_2-1])
soup3=BeautifulSoup(req3.content,'html.parser')
junk=soup3.findAll(class_=re.compile("original-line"))
junk2=soup3.findAll(class_=re.compile("modern-line"))
junky2=soup3.findAll(class_=re.compile("noFear-right"))
junky=soup3.findAll(class_=re.compile("noFear-left"))
junky.pop(0)
junky2.pop(0)
junk.pop(0)
junk2.pop(0)
with open(filename+actname+".txt",'a') as opf :
            opf.write("MODREN VERSION :"+'\n')
i=0
for i in range(len(junk2)):
        scrap2=junk2[i]
        _=junky2[i]
        san=str(scrap2)
        san=san.split('">')
        san= san[1]
        san=san.split("</div>")
        try:
            _=str(_)
            _= _.split('<b>')
            _=_[1]
            _=_.split('</b>')
            _=_[0]
        except:
            _=" "

        with open(filename+actname+".txt",'a') as opf:

            opf.write(_+':')
            opf.write(san[0]+'\n')
opf.close()
with open(filename+actname+".txt",'a') as opf :
            opf.write("SHAKY VERSION :"+'\n')
for i1 in range(len(junk)):
        scrap=junk[i1]
        __=junky[i]
        san=str(scrap)
        san=san.split('">')
        san= san[1]
        san=san.split("</div>")
        try:
            __=str(__)
            __=__.split('<b>')
            __=__[1]
            __=__.split('</b>')
            __=__[0]
        except:
            __=" "
        with open(filename+actname+".txt",'a') as opf:
            opf.write(__+": ")
            opf.write(san[0]+'\n')


al=[]
for a in temp4:
        a=str(a)
        a=a.split('_')
        a=a[1]
        a=a.split('.')
        a=a[0]
        al.append(int(a))


i=0

for i in range(al[0],al[-1],2):
        print i
        url=bucket_url[choice-1]+"page_"+str(i)+".html"
        r=requests.get(url)
        soup=BeautifulSoup(r.content,'html.parser')
        junk2=soup.findAll(class_=re.compile("original-line"))
        junk=soup.findAll(class_=re.compile("modern-line"))
        junky=soup.findAll(class_=re.compile("noFear-left"))
        junky2=soup.findAll(class_=re.compile("noFear-right"))
        junky2.pop(0)
        junky.pop(0)
        op=open(filename+'.txt','a')
        op.write("Shakky version \n")

        for i3 in range(len(junk2)):
                scrap2=junk2[i3]

                san=str(scrap2)
                san=san.split('">')
                san= san[1]
                san=san.split("</div>")
                try:
                    _=junky[i3]
                    _=str(_)
                    _= _.split('<b>')
                    _=_[1]
                    _=_.split('</b>')
                    _=_[0]+":"
                except:
                    _=""
                op=open(filename+'.txt','a')
                op.write(_)
                op.write(san[0]+'\n')
                op.close()
        op=open(filename+'.txt','a')
        op.write("Modern version \n")
        i4=0
        for i4 in range(len(junk)):
                scrap2=junk[i4]
                san=str(scrap2)

                san=san.split('">')
                san= san[1]
                san=san.split("</div>")
                try:
                    _=junky[i4]
                    _=str(_)
                    _= _.split('<b>')
                    _=_[1]
                    _=_.split('</b>')
                    _=_[0]
                except:
                    _=" "

                with open(filename+actname+".txt",'a') as opf:

                    opf.write(_+':')
                    opf.write(san[0]+'\n')

        # url="http://nfs.sparknotes.com/errors/page_"+str(i)+".html"















#
# for i in range(len(junk2)):
#         scrap2=junk2[i]
#         _=junky2[i]
#         san=str(scrap2)
#         san=san.split('">')
#         san= san[1]
#         san=san.split("</div>")
#         try:
#             _=str(_)
#             _= _.split('<b>')
#             _=_[1]
#             _=_.split('</b>')
#             _=_[0]
#         except:
#             _=" "
#
#         with open(filename+actname+".txt",'a') as opf:
#
#             opf.write(_+':')
#             opf.write(san[0]+'\n')
#
#
#
#













# for scrap in junk:
#              tempo=str(scrap)
#              tempo=tempo.split('<b>')
#              tempo=tempo[1]
#              tempo=tempo.split('</b>')
#              tempo=tempo[0]
#              san=str(scrap)
#              san=san.split('">')
#              san= san[1]
#              san=san.split("</div>")
#
#              with open('test_case.txt','a') as opf:
#                  opf.write("SHAKE VERSION :")
#                  opf.write(tempo)
#                  opf.write(san[0]+'\n')
# #                  i+=1
# for scrap2 in junk2:
#         san=str(scrap2)
#         san=san.split('">')
#         san= san[1]
#         san=san.split("</div>")
#         with open('test_case.txt','a') as opf:
#             opf.write("MODREN VERSION :")
#             opf.write(san[0]+'\n')
# opf.close()

# for urls in bucket_url:
#         new_url=urls
#         new_req=requests.get(str(new_url))
#         soup2=BeautifulSoup(new_req.content,'html.parser')
#         temp4=soup2.find_all(href=re.compile("page"))
#         for tagss in temp4:
#             temp5=str(tagss)
#             temp5=temp5.split('<a href="')
#             temp5=temp5[1]
#             temp5=temp5.split('">')
#             new_bucket.append(temp5[0])

#print temp4for tagss in temp4:
    # temp5=str(tagss)
    # temp5=temp5.split('<a href="')
    # temp5=temp5[1]
    # temp5=temp5.split('">')
    # new_bucket.append(temp5[0])
