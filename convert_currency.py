import requests
from bs4 import BeautifulSoup

#url = f'https://wise.com/gb/currency-converter/{from}-to-{to}-rate?amount={amount}'

url = 'https://wise.com/gb/currency-converter/'

def convert_currency(inp):
  from_cur = inp['from_cur']
  to_cur = inp['to_cur']
  amount = inp['amount']
  query_statement = f"{from_cur.lower()}-to-{to_cur.lower()}-rate?amount={amount}"
  result = requests.get(url+query_statement)
  if result.status_code == 200:
    soup = BeautifulSoup(result.text, "html.parser")

    #inp_target = soup.find("input",{"id":"cc-amount-to"})
    rate = soup.find("h3", {"class":"cc__source-to-target"}).find("span",{"class":"text-success"}).text
    rate = float(rate)

    target_amount = rate * amount
    return {"from_cur":from_cur, "to_cur":to_cur, "from_amount" : amount, "to_amount": target_amount}
  else:
    print("Faild to connect to the server. Please try it again later.")
