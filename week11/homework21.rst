===================
Домшанее задание 21
===================

Материалы занятия:  https://github.com/maxchv/LearnPython/tree/master/week21

Слайды:	            https://github.com/maxchv/LearnPython/tree/master/week21/intro_django.pptx

Примеры на занятии: https://github.com/maxchv/LearnPython/tree/master/week21/examples/startweb
					https://github.com/maxchv/LearnPython/tree/master/week21/examples/website

Домашнее задание:  

	* Установить django
	* Создайть проект website
	* Создайть приложение hello
	* Создайть метод представления с именем index в файле views.py, который должен
	  возвращать HttpResponse с приветственным сообщением "Добро пожаловать" (заголовок 
	  первого урованя h1), заголовком (title) "Учим django"
	* Добавить привязки путей / и /hello к созданному представлению
	  в файлах urls.py и /hello/urls.py
	* Создать второй метод представления about, который должен возвращать HttpResponse с
	  Вашим резюме. Добавить заголовок (title) О нас
	* Привязать это представление к /hello/about в файле /hello/urls.py
	* Добавить гипертекстовую ссылку (<a href="about">О нас</a>) на страницу about в 
	  HttpResponse представления index	  
	* В HttpResponse представления about добавить гипертекстовую ссылку На главную, которая
      должна вести на страницу представления index (/hello)

Примеры на занятии: https://github.com/maxchv/LearnPython/tree/master/week21
		

Видео: 		https://youtu.be/MYnEJ907z-Y https://youtu.be/wGPGNXefZRQ