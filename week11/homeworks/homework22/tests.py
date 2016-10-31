from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from website import settings
import os.path
from blog import views
import re


class TestProject(TestCase):
    def test_project_name(self):
        self.assertEqual("website", os.path.basename(settings.BASE_DIR),
                         "Отсутствует проект website")

    def test_application(self):
        path = os.path.join(settings.BASE_DIR, "blog")
        self.assertTrue(os.path.exists(path),
                        "Отстутвует приложение blog")
        self.assertTrue('blog' in settings.INSTALLED_APPS,
                        "Не добавлено приложение blog в список INSTALLED_APPS")

    def test_templates_dir(self):
        path = os.path.join(settings.BASE_DIR, "templates")
        self.assertTrue(os.path.exists(path),
                        "Отстутвует директория templates")

        path = os.path.join(path, "blog")
        self.assertTrue(os.path.exists(path),
                        "Отстутвует директория templates/blog")

    def test_settings_templates(self):
        path = os.path.join(settings.BASE_DIR, "templates")
        self.assertTrue(path in settings.TEMPLATES[0]['DIRS'],
                        "Не настроен путь к диретории с шаблонами в TEMPLATES[0]['DIRS']")

    def test_exists_static_dirs(self):
        path = os.path.join(settings.BASE_DIR, "static")
        self.assertTrue(os.path.exists(path),
                        "Отсутствует директория static")

        path = os.path.join(path, "blog")
        self.assertTrue(os.path.exists(path),
                        "Отсутствует директория static/blog")

    def test_settings_static_dir(self):
        path = os.path.join(settings.BASE_DIR, "static")
        self.assertTrue(path in settings.STATICFILES_DIRS,
                        "Отстутсвуют настройки статических файлов в STATICFILES_DIRS")

    def test_exists_css_dir(self):
        css_path = os.path.join(settings.BASE_DIR, "static", "blog", "css")
        self.assertTrue(os.path.exists(css_path),
                        "Отсутствует диретория static/blog/css")
        path = os.path.join(css_path, "blog-home.css")
        self.assertTrue(os.path.exists(path),
                        "Отсутствует файл static/blog/css/blog-home.css")
        path = os.path.join(css_path, "blog-post.css")
        self.assertTrue(os.path.exists(path),
                        "Отсутствует файл static/blog/css/blog-post.css")
        path = os.path.join(css_path, "bootstrap.css")
        self.assertTrue(os.path.exists(path),
                        "Отсутствует файл static/blog/css/bootstrap.css")
        path = os.path.join(css_path, "bootstrap.min.css")
        self.assertTrue(os.path.exists(path),
                        "Отсутствует файл static/blog/css/bootstrap.min.css")

    def test_exists_js_dir(self):
        js_path = os.path.join(settings.BASE_DIR, "static", "blog", "js")
        self.assertTrue(os.path.exists(js_path),
                        "Отсутствует диретория static/blog/js")

        path = os.path.join(js_path, "bootstrap.js")
        self.assertTrue(os.path.exists(path),
                        "Отсутствует файл static/blog/js/bootstrap.js")

        path = os.path.join(js_path, "bootstrap.min.js")
        self.assertTrue(os.path.exists(path),
                        "Отсутствует файл static/blog/js/bootstrap.min.js")

        path = os.path.join(js_path, "jquery.js")
        self.assertTrue(os.path.exists(path),
                        "Отсутствует файл static/blog/js/jquery.js")

    def test_exists_fonts_dir(self):
        fonts_path = os.path.join(settings.BASE_DIR, "static", "blog", "fonts")
        self.assertTrue(os.path.exists(fonts_path),
                        "Отсутствует диретория static/blog/fonts")

    def test_exists_templates_file(self):
        base = os.path.join(settings.BASE_DIR, "templates", "blog")
        path = os.path.join(base, "base.html")
        self.assertTrue(os.path.exists(path),
                        "Отсутствует файл templates/blog/base.html")
        path = os.path.join(base, "index.html")
        self.assertTrue(os.path.exists(path),
                        "Отсутствует файл templates/blog/index.html")
        path = os.path.join(base, "post.html")
        self.assertTrue(os.path.exists(path),
                        "Отсутствует файл templates/blog/post.html")


class TestBlog(TestCase):
    def test_index_route(self):
        index = resolve("/blog/")
        self.assertEqual(index.func, views.index)

    def test_index_route(self):
        index = resolve("/blog/post/")
        self.assertEqual(index.func, views.post)

    def test_static_links(self):
        request = HttpRequest()
        response = views.index(request)
        self.assertFalse(re.match(r"^<!doctype\s+html>",
                                  response.content.decode("utf-8"),
                                  re.IGNORECASE) is None)

