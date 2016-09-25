import re
import urllib.request as request

p = re.compile(r'<article>[^<]+<[^<]+<a\s+href=[\'"](\S+?)[\'"]?>\s*([^<]+?)\s*<')
test_str = "<article>\n            <h2>\n                <a href=\"https://dou.ua/lenta/digests/information-security-digest-2/\">\n\n                    Information Security дайджест #2: Кибервойна и&nbsp;удары украинских хактивистов, зима близко: заклеиваем окна и&nbsp;веб-камеры\n\n                            <img class=\"announce-img\" src=\"https://s.dou.ua/img/announces/120x_sec2_ilS17RM.png\" srcset=\"https://s.dou.ua/img/announces/240x_sec2_ilS17RM.png 2x\" alt=\"Information Security дайджест #2: Кибервойна и&nbsp;удары украинских хактивистов, зима близко: заклеиваем окна и&nbsp;веб-камеры\">\n                </a>\n            </h2>\n\n            <div class=\"b-info\">\n                <a class=\"author\" href=\"https://dou.ua/users/egor-papyishev/\">Егор Папышев</a>\n                <time class=\"date\">23 сентября<span class=\"m-hide\">, 12:54</span></time>\n                <span class=\"pageviews\" title=\"Количество просмотров\">2604</span>\n            </div>\n\n                <p class=\"b-typo\">\n                    В&nbsp;выпуске: новости с&nbsp;фронтов кибервойны, анонсы предстоящих конференций в&nbsp;сфере&nbsp;ИБ, критическое обновление Tor, компрометация продавцов в&nbsp;даркнете, новые инструменты скимминга, ботнеты из&nbsp;смартфонов против контакт-центров, USB Kill версии два поджарит вас за&nbsp;секунду, директор ФБР советует запасаться скотчем и&nbsp;многое другое.&nbsp;<a href=\"https://dou.ua/lenta/digests/information-security-digest-2/#comments\" class=\"g-comments-round __lazy\" data-id=\"41468\">7</a>\n                </p>\n\n            <div class=\"more\">\n                <a class=\"topic\" href=\"https://dou.ua/lenta/digests/\">Ссылки</a>\n                    <em class=\"dot\">·</em> <a href=\"https://dou.ua/lenta/tags/Information%20Security%20%D0%B4%D0%B0%D0%B9%D0%B4%D0%B6%D0%B5%D1%81%D1%82/\">Information Security дайджест</a>, <a href=\"https://dou.ua/lenta/tags/%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D0%BE%D1%81%D1%82%D1%8C/\">безопасность</a>\n            </div>\n        </article>"

# headers = re.findall(p, test_str)
# print(headers[0][1])
# print(headers[0][0])

#with open('dou.html', encoding='utf8') as f:

f = request.urlopen("https://dou.ua/lenta/page/2/")
bhtml = f.read()
html = bhtml.decode("utf8")
headers = p.findall(html)
for header in headers:
    print(header)

with open("result.html", "w", encoding="utf8") as r:
    r.write("<html>"
                "<head>"
                    "<title>Result</title>"
                    "<meta charset='utf8' />"
                "</head>"
            "<body>"
            "<h1>Result</h1>"
            "<ul>")
    for header in headers:
        r.write("<li><a href='"+header[0]+"'>")
        r.write(header[1] + "</a></li>")
    r.write("</ul></body></html>")

