# import requests
# from bs4 import BeautifulSoup
# def noticias():
#     url = 'https://www.globo.com/'
#     pagina = requests.get(url)
#     soup = BeautifulSoup(pagina.content, 'html.parser')
#     # Encontrar todos os h2 com a classe 'post_title'
#     noticia_elements = soup.find_all('h2', class_='post__title')
#     print(noticia_elements)
#     #até aqui fiz corretamente.
#     disc = {}
#     if noticia_elements:
#         for noticia in noticia_elements:
#             a_tag = noticia.find('a')
#             if a_tag:
#                 titulo = a_tag.get_text(strip=True)
#                 link = a_tag.get('href')
#                 if titulo and link:
#                     disc[titulo] = link
#     else:
#         print("Nenhuma notícia encontrada com a classe 'post_title'.")
#     return disc
# news = noticias()

# print(news)

from bs4 import BeautifulSoup
import requests


data = []
response = requests.get("https://www.globo.com/")
soup = BeautifulSoup(response.content, 'html.parser')
titles = soup.find_all('h2', class_="post__title")

for news in titles:
    data.append({
        "title": news.string,
        "link": news.parent['data-tracking-label']
    })
print(data)

print(titles)
