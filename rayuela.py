import html2text, requests
h = html2text.HTML2Text()

# Ignore HTML attributes
h.ignore_links = True
h.ignore_emphasis= True
h.ignore_images= True
h.ignore_links= True
h.ignore_tables= True

url1 = 'http://www.literaberinto.com/Cortazar/rayuela'
url2 = '.htm'
urls = [url1+str(i)+url2 for i in range(1,57)]

corpus = open('rayuela.txt','a+')

for chp,url in enumerate(urls):
  r = requests.get(url)
  print('Descargando capítulo #' + str(chp + 1) + '...')
  body = h.handle(r.text).split('* * *')
  
  corpus.write(body[0]+'\n')

corpus.close()
