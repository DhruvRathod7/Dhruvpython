import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

question = soup.select(".quesion-summary")
for question in question:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())

