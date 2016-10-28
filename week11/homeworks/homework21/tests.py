from django.core.urlresolvers import resolve
from django.test import TestCase
from .views import index, about
from django.http import HttpRequest

class HomePageTest(TestCase):
    def test_index_route(self):
        """  
        Добавить привязки путей / и /hello к созданному представлению
        в файлах urls.py и /hello/ursl.py
        """
        root = resolve('/')
        self.assertEqual(root.func, index)
        hello = resolve('/hello/')
        self.assertEqual(hello.func, index)

    def test_title_in_index(self):
        """
        Создайть метод представления с именем index в файле views.py, который должен
        возвращать HttpResponse с заголовком (title) "Учим django"
        """        
        request = HttpRequest()
        response = index(request)
        self.assertTrue(response.content.startswith(b'<!doctype html>'))
        self.assertIn(bytes('<title>Учим django</title>', "utf-8"), response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

    def test_h1_in_index(self):
        """
        Создайть метод представления с именем index в файле views.py, который должен
        возвращать HttpResponse с приветственным сообщением "Добро пожаловать" (заголовок 
        первого урованя h1), заголовком (title) "Учим django", а также гипертекстовой ссылкой
        на страницу hello/about
        """        
        request = HttpRequest()
        response = index(request)
        self.assertIn(bytes('<h1>Добро пожаловать</h1>', "utf-8"), response.content)
        
    def test_link_index_to_about(self):
        """
        Добавить гипертекстовую ссылку (тег a) на страницу about в HttpResponse представления index
        """
        request = HttpRequest()
        response = index(request)
        self.assertIn(bytes('<a href="about">О нас</a>', "utf-8"), response.content)

class AboutPageTest(TestCase):
    def test_about(self):
        """
        Создать второй метод представления about, который должен возвращать HttpResponse с
        Вашим резюме. Добавить заголовок (title) О нас
        """
        request = HttpRequest()
        response = about(request)
        self.assertIn(bytes("<title>О нас</title>","utf-8"), response.content)

    def test_about_route(self):
        """
        Привязать это представление к /hello/about в файле /hello/urls.py
        """
        found = resolve('/hello/about/')
        self.assertEqual(found.func, about)

    def test_link_about_to_index(self):
        """
        В HttpResponse представления about добавить гипертекстовую ссылку На главную, на страницу index
        """
        request = HttpRequest()
        response = about(request)
        self.assertIn(bytes('<a href="/hello">На главную</a>', "utf-8"), response.content)
