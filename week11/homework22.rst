===================
Домшанее задание 22
===================

Материалы занятия:  https://github.com/maxchv/LearnPython/tree/master/week11

Слайды:	            https://github.com/maxchv/LearnPython/tree/master/week11/templates.pptx

Домашнее задание:   

	1) 	Создать проект website
	2) 	В проект добавить приложение blog
	3) 	В файле настроек settings.py добавить приложение blog в список приложений проекта
	4) 	В проекте создать директорию templates
	5) 	В директории templates создать директорию blog
	6) 	В файле настроек settings.py прописать путь к директории с шаблонами templates
	7) 	В директории проекта создать директорию static и static/blog
	8) 	Добавить настройки в файл settings.py для указания местоположения директории статических файлов
	9) 	Распаковать архив https://github.com/maxchv/LearnPython/blob/master/week11/homeworks/tempalte.rar 
		во временную директорию
	10)	Скопировать директории css, fonts и js в static/blog
	11) Поместить файлы index.html и post.html в директорию templates/blog
	12) На базе файлов index.html и post.html создать общий шаблон base.html
	13) В базовом шаблоне base.html необходимо:
			а) подгрузить статические файлы
			б) изменить ссылки в атрибуте href в тегах link и атрибут src в тегах script
			в) содержимое элемента div с классом col-md-8 заменить на блок {% block content %}{% endblock %}
	14) В файлах index.html и post.html необходимо:
			а) наследовать шаблон base.html
			б) из содердимого оставить только то, что входило в <div class="col-md-8">
			в) поместить это содержимое в блок content
			г) Обновить ссылки с post.html на post и с index.html на /blog
	15) Добавить представление index в файле blog/views.py, которое должно возвращать 
		отрендеренный шаблон blog/index.html
	16) Добавить привязку представления index к пути blog/
	17) Добавить представление post в файле blog/views.py, которое должно возвращать 
		отрендеренный шаблон blog/post.html
	18) Добавить привязку представления post к пути blog/post

Примеры на занятии: https://github.com/maxchv/LearnPython/tree/master/week11/examples/website
		

Видео: 				https://youtu.be/P_B8X11vdzI