from newspaper import Article
import json

naver_news_url = "https:\/\/www.joongangenews.com\/news\/articleView.html?idxno=412671"

url = json.loads(f'"{naver_news_url}"')

article = Article(url, language="ko")
article.download()
article.parse()

print("제목: ", article.title)
print("\n본문: ", article.text)
print("\n출처: ", url)

