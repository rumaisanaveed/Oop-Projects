#-------------------------------------------------------------------------------------------------------------------------------
# Download images
from urllib import request
url = 'http://www.w3schools.com'
y = url.find("/",8)
seed = url[0:y]
a = request.urlopen(url)
b = a.read().decode()
c = b.split()

def saveImage(imageUrl):
            s = imageUrl.rfind("/")
            fileName = imageUrl[s + 1:]
            imageConn = request.urlopen(imageUrl)
            imageBytes = imageConn.read()
            saveImage = open(fileName,"wb")
            saveImage.write(imageBytes)
            saveImage.close()
for x in c:
    if x.startswith('src'):
        d = x.replace("'",'"').split('"')
        if d[1].startswith('https'):
            imgUrl = d[1]
            saveImage(imgUrl)
        else:
             imgUrl = seed + d[1]
             saveImage(imgUrl)
             
#------------------------------------------------------------------------------------------------------------------------------
from urllib import request

url = "www.example.com/"
a = request.urlopen(url)
b = a.read()
c = b.split()
for i in c:
    if i.startswith("href"):
        d = i.split('"')
        print(d[1])
#------------------------------------------------------------------------------------------------------------------------------
# Extract links 
from urllib import request
url = 'http://www.w3schools.com'
a = request.urlopen(url)
b = a.read().decode()
c = b.split()
print('-------LINKS-------')
for x in c:
    if x.startswith('href'):
        d = x.replace("'",'"').split('"')
        if d[1].startswith('https'):
            print(d[1])
        else:
            print(url+d[1])
print('-------IMAGES-------')
for x in c:
    if x.startswith('src'):
        d = x.replace("'",'"').split('"')
        if d[1].startswith('https'):
            print(d[1])
        else:
            print(url+d[1]) 
#--------------------------------------------------------------------------------------------------------------------------------
