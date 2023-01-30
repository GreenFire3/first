import  requests
from bs4 import BeautifulSoup

url = 'https://qna.habr.com/q/465548'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

data = soup.find('div', class_="answer__text js-answer-text").text
print(data)



#for i in data:
#    name = i.find('span', class_="text").text
#    print(name)
#    print('f')



