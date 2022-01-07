import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# send the request
response = requests.get(URL)
webpage = response.text

# make soup
soup = BeautifulSoup(webpage, "html.parser")

# get all movie titles - h3 class="title"
all_movies = soup.find_all(name="h3", class_="title")

# print title and name of the movie
for movie in all_movies[::-1]:
    print(movie.getText())
