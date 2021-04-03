import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"

def get_table_row(url):
  result = requests.get(url)
  soup= BeautifulSoup(result.text,"html.parser")

  table = soup.find("table",{"class":"table"})
  return table.find("tbody").find_all("tr")

def extract_country_currency(html):
  table_col=html.find_all("td")
  country_name=table_col[0].get_text()
  currency_code=table_col[2].get_text()
  return({"country":country_name, "currency":currency_code})



def get_country_currency():
  table_row = get_table_row(url)

  country_currency=[]
  for tr in table_row:
    country_currency.append(extract_country_currency(tr))
  return country_currency