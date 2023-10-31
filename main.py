from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name='span', class_='titleline')
scores = soup.find_all(name='span', class_='score')

article_text = []
article_link = []
score_list = []

for article in articles:
    article_text.append(article.getText())
    article_link.append(article.find(name='a').get('href'))

# for score in scores:
#     score_list.append(score.getText())

# using list comprehension below
score_list = [int(score.getText().split()[0]) for score in scores]

# Need to convert the score list to integers but we have to split off the 'points' string first
# first_item = int(score_list[0].split()[0])
top_score = max(score_list)
top_score_index = score_list.index(top_score)

# below we want to print out the article title and link with the highest score
print(article_text[top_score_index])
print(article_link[top_score_index])
print(top_score)





# below was the code to parse the website.html file
# with open('website.html', encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
# # .a prints first anchor tag
# # print(soup.a)
# anchor_tags = soup.find_all(name='a')
# print(anchor_tags)
#
# for tag in anchor_tags:
#     # print(tag.getText())
#     print(tag.get('href'))
#
# heading = soup.find(name='h1', id='name')
# print(heading)
#
# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading)
# print(section_heading.text)
# print(section_heading.name)
# print(section_heading.get('class'))
#
# # below searches for an a tag inside a p tag. you can also use the class or id in the selector. select_one only
# # selects the first item that meets the criteria
# company_url = soup.select_one(selector='p a')
# name = soup.select_one(selector='#name')
# # below selects all of the items that match
# headings = soup.select(selector='.heading')
# print(headings)