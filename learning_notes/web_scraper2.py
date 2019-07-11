import requests
from bs4 import BeautifulSoup, SoupStrainer


url = 'https://www.dailysmarty.com/topics/python'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

posts = []
links = []

for line in soup.find_all('a'):
    links.append(line.get('href'))

for word in links:
    if word.startswith('/posts'):
        posts.append(word)

print(posts)
