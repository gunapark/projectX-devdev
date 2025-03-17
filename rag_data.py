import requests
from bs4 import BeautifulSoup
import sys
import re
import spacy

nlp = spacy.load("ko_core_news_md")
news_url = "https://mypetlife.co.kr/141906/"

print(news_url)

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(news_url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

article_body = soup.select_one(".entry-content.entry.clearfix")

if article_body:
    # ✅ HTML 태그 없이 순수한 텍스트만 가져오기 (줄바꿈 포함)
    raw_text = article_body.get_text(separator="\n", strip=True)
    # ✅ 불필요한 줄바꿈 제거 (빈 줄 제거 + 여러 개의 줄바꿈을 하나로 정리)
    cleaned_text = "\n".join(line.strip() for line in raw_text.splitlines() if line.strip())
    text = re.sub(r"비마이펫 Q&A 커뮤니티[\s\S]*", "", cleaned_text)
    text = text.strip()

else:
    print("❌ 본문을 찾을 수 없습니다.")


def chunk_text_by_sentence(text, max_chunk_size=512):
    doc = nlp(text)
    chunks = []
    current_chunk = ""

    for sent in doc.sents:
        if len(current_chunk) + len(sent.text) <= max_chunk_size:
            current_chunk += " " + sent.text
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sent.text

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

chunks = chunk_text_by_sentence(text)
for i, chunk in enumerate(chunks):
    print(f"청크 {i+1}: {chunk}")