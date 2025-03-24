import feedparser

# URL новостной ленты
# url = 'https://moex.com/export/news.aspx?cat=100'
url = 'https://smart-lab.ru/allblog/'

# Загрузка и разбор новостной ленты
feed = feedparser.parse(url)

# Вывод заголовков новостей из ленты
for entry in feed.entries:
    print(entry.title)


