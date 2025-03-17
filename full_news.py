import requests
from bs4 import BeautifulSoup

# ✅ 크롤링할 웹페이지 URL
news_url = "https://mypetlife.co.kr/141906/"

# ✅ User-Agent 설정 (크롤링 차단 방지)
headers = {"User-Agent": "Mozilla/5.0"}

# ✅ 페이지 요청
response = requests.get(news_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# ✅ 페이지에서 모든 텍스트 가져오기
text_only = soup.get_text(separator="\n", strip=True)  # 줄바꿈 유지 & 공백 제거

print(text_only)
