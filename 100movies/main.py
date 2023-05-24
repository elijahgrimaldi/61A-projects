from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/", headers={"User-Agent": "Requests"})
print(response.text)
# soup = BeautifulSoup(movies_web_page, "html.parser")
# movie_name = soup.find_all("h3")
# print(movie_name)