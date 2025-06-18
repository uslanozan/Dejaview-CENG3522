import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver

dictionary = {"category": [], "title": [], "content": []}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

url = f"https://tr.wikipedia.org/wiki/Türkiye%27de_anayasal_süreç"

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(5)

source = driver.page_source
soup = BeautifulSoup(source, 'html.parser')

headings = soup.find_all("div", class_="mw-heading mw-heading3")

results = []

for heading in headings:
    title = heading.get_text(strip=True)

    next_el = heading.find_next_sibling()
    while next_el and next_el.name != "p":
        next_el = next_el.find_next_sibling()

    if next_el and next_el.name == "p":
        paragraph = next_el.get_text(strip=True)
        results.append((title, paragraph))

for result in results:
    dictionary["category"].append("Siyasi")
    dictionary["content"].append(result[1])
    dictionary["title"].append(result[0])

driver.quit()

df = pd.DataFrame.from_dict(dictionary)
df.to_csv("anayasal.csv", index=False, encoding="utf-8-sig")
