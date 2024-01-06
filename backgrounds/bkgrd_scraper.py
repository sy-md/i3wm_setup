import requests
from bs4 import BeautifulSoup
#URL1 = "https://www.pixiv.net/"
#URL2 = "https://www.pixiv.net/en/users/63601519/bookmarks/artworks"
URL3 = "https://accounts.pixiv.net/login?return_to=https%3A%2F%2Fwww.pixiv.net%2Fen%2Fusers%2F63601519%2Fbookmarks%2Fartworks&lang=en&source=pc&view_type=page"
#have to use a post to login

"""
sends a post to url3 then youll be brought to url2

"""
r = requests.get(URL3)

soup = BeautifulSoup(r.content, 'html5lib') 

print(soup.prettify())

