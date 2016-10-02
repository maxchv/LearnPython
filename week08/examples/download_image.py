Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> url = 'http://itstep.dp.ua/wp-content/uploads/2016/09/shapka.jpg'
>>> import urllib.request as r
>>> data = r.urlopen(url)
>>> img = data.read()
>>> img[:10]
b'\xff\xd8\xff\xe1(tExif'
>>> with open(r'd:\shapka.jpg', 'wb') as f:
	f.write(img)

	
332012
>>> 
