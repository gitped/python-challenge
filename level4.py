import urllib.request
import urllib.parse

pageID = '12345'
for cont in range(400):
  params = urllib.parse.urlencode({'nothing': pageID})
  url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?' + params
  mssg = urllib.request.urlopen(url)
  mssg = mssg.read().decode('utf-8')
  
  print(str(cont+1) + ' ---> ' + mssg)

  pos = mssg.find('and the next nothing is ')
  if pos > -1:
    pageID = mssg[pos+24:]
  else:
    pageID = int(pageID)//2
