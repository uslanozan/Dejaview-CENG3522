import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver

dictionary = {"category": [], "title": [], "content": []}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

url = f"https://tr.wikipedia.org/wiki/Kategori:Yıla_göre_Türkiye%27de_spor"

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(5)

source = driver.page_source
soup = BeautifulSoup(source, 'html.parser')

lis = []
content_div = soup.find_all("div", {"class": "mw-content-ltr", "dir": "ltr"})[1]
if content_div:
    category_groups = content_div.find_all("div", class_="mw-category-group")[1:]
    
    for group in category_groups:
        bdi_tags = group.find_all("bdi", dir="ltr")
        for bdi in bdi_tags:
            a_tag = bdi.find("a")
            if a_tag and a_tag.get("href"):
                full_url = "https://tr.wikipedia.org" + a_tag.get("href").strip()
                lis.append(full_url)

lis2 = []
for li in lis:
    driver.get(li)
    time.sleep(3)
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')

    div = soup.find("div",id="mw-pages")
    if div:
        liss = div.find_all("li")
        if liss:
            for li in liss:
                lis2.append("https://tr.wikipedia.org" + li.find("a").get("href").strip()) if li.find("a") and li.find("a").get("href") else None

for link in lis2:
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

        dictionary["category"].append("Spor")
        dictionary["title"].append(title_tag.text)
        dictionary["content"].append(first_paragraph)
    except Exception as e:
        print(f"error: {e}")
        continue

driver.quit()

df = pd.DataFrame.from_dict(dictionary)
df.to_csv("spor.csv", index=False, encoding="utf-8-sig")
