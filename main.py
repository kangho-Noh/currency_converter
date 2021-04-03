import os
import requests
from bs4 import BeautifulSoup

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

def show_interface(country_currency):
  print("Hello! Please choose a country by number: ")

  country_length = len(country_currency)
  for i in range(country_length):
    print(f"# {i+1} {country_currency[i]['country']}")

  
  while 1:
    try:
      inp = int(input("#: "))
      if inp > country_length or inp< 1:
        print("Choose a number from the list.")
      else:
        print(f"you chose {country_currency[inp-1]['country']}")
        print(f"The currency code is {country_currency[inp-1]['currency']}")
        break
    except:
      print("That wasn's a number.")

def main():
  os.system("clear")
  url = "https://www.iban.com/currency-codes"

  table_row = get_table_row(url)

  country_currency=[]
  for tr in table_row:
    country_currency.append(extract_country_currency(tr))

  show_interface(country_currency)
  

main()
  

