import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# send the request
response = requests.get(URL)
webpage = response.text

# make soup
soup = BeautifulSoup(webpage, "html.parser")

# debug
print(soup)


