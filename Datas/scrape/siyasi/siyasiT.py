import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver

dictionary = {"category": [], "title": [], "content": []}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

url = f"https://tr.wikipedia.org/wiki/Kategori:Türkiye_siyasi_tarihi"

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(5)

source = driver.page_source
soup = BeautifulSoup(source, 'html.parser')

mainTable = soup.find("div", {"id": "mw-pages"})
mainTable = mainTable.find("div",class_="mw-category mw-category-columns")
a_s = mainTable.find_all("li")

lis = []
for a in a_s:
    lis.append("https://tr.wikipedia.org" + a.find("a").get("href").strip()) if a.find("a") and a.find("a").get("href") else None

for link in lis:
    try:
        driver.get(link)
        time.sleep(3)
        source = driver.page_source
        soup = BeautifulSoup(source, 'html.parser')

        title_tag = soup.find("span", {"class": "mw-page-title-main"})
        if not title_tag:
            continue

        div = soup.find("div", {"class": "mw-content-ltr mw-parser-output"})
        if not div:
            continue

        paragraphs = div.find_all("p")
        first_paragraph = next((p.text.strip() for p in paragraphs if p.text.strip()), "")

        dictionary["category"].append("Siyasi")
        dictionary["title"].append(title_tag.text)
        dictionary["content"].append(first_paragraph)
    except Exception as e:
        print(f"error: {e}")
        continue

driver.quit()

df = pd.DataFrame.from_dict(dictionary)
df.to_csv("SiyasiTarihi.csv", index=False, encoding="utf-8-sig")
