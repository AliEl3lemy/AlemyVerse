import requests
from bs4 import BeautifulSoup
import pandas as pd
print("Connecting to website and extracting all quotes")
url = "http://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
quotes_boxes = soup.find_all("div", class_="quote")
scraped_data = []
for box in quotes_boxes:
    quote_text = box.find("span", class_="text").text
    author_name = box.find("small", class_="author").text
    scraped_data.append({
        "Quote": quote_text,
        "Author": author_name
})
df = pd.DataFrame(scraped_data)
df.to_csv("quotes_data.csv", index=False, encoding="utf-8-sig")
print("\n--- Sucess! Data Extracted and saved to 'quotes_data.csv' ---")
print(df.head())