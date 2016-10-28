===================
Домшанее задание 21
===================

Материалы занятия:  https://github.com/maxchv/LearnPython/tree/master/week21

Слайды:	            https://github.com/maxchv/LearnPython/tree/master/week21/intro_django.pptx

Домашнее задание:  

	* Установите django
	* Создайте проект website
	* Создайте приложение hellodjango
	* Создайте метод представление с именем index в файле views.py, который должен
	  возвращать HttpResponse с приветственным сообщением "Добро пожаловать" (заголовок 
	  первого урованя h1), заголовком (title) "Учим django", а также гипертекстовой ссылкой
	  на страницу hellodjango/about
	* Добавте привязки маршрутов /hellodjango и /hellodjango/index к созданным представлением
	  в файлах urls.py и /hellodjango/ursl.py
	  
	• Create a new view method called about which returns the following HttpResponse:
'Rango says here is the about page.'
	• Map this view to /rango/about/. For this step, you’ll only need to edit the urls.py
of the Rango application. Remember the /rango/ part is handled by the projects
urls.py.
	• Revise the HttpResponse in the index view to include a link to the about page.
	• In the HttpResponse in the about view include a link back to the main page. 

Примеры на занятии: https://github.com/maxchv/LearnPython/tree/master/week21
		

Видео: 	